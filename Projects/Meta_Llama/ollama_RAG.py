'''Example of using ollama with FireCrawl in Langchain'''

import os
os.environ['LANGCHAIN_TRACING-V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = 'xxxxx'

local_llm = 'llama3'

### Document Retrieval
import langchain.text_splitter as text_splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.document_loaders import FireCrawlLoader
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain.docstore.document import Document

urls = ["https://www.ai-jason.com/learn-ai/how-to-reduce-llm-cost",
        "https://www.ai-jason.com/learn-ai/gpt5-llm",
        "https://www.ai-jason.com/learn-ai/how-to-build-ai-agent-tutorial-3",
]
# use FireCrawl to cycle through URLs
docs = [FireCrawlLoader(api_key='xxxxx', url=url, mode = 'scrape').load() for url in urls]

# Split documents
docs_list = [item for sublist in docs for item in sublist]
text_splits = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chuck_size=250, chuck_overlap= 0)
doc_splits = text_splitter.split_documents(docs_list)

# Complex meta data filter
filtered_docs =[]
for doc in doc_splits:
    # Ensure the doc is an instance of the Dcouemnt and has a 'metadata' attribute
    if isinstance(doc,Document) and hasattr(doc, 'metadata'):
        clean_metadta = {k: v for k, v in doc.metadata.items() if isinstance(v, (str,int,float,bool))}
        filtered_docs.append(Document(page_content=doc.page_content, metadata = clean_metadta))

# add to VectorDB
vectorstore = Chroma.from_documents(
    documents=filtered_docs, 
    collection_name = 'rag-chroma', 
    embedding=GPT4AllEmbeddings(),
)

retriever = vectorstore.as_retriever()

### Retrieval Grader
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import JsonOutputParser

# LLM
llm = ChatOllama(model=local_llm, format='json', temperature=0)

prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a grader assessing relevance of a 
    retrieved document to a user question. If the document contains keywords related to the user qeustion, grade it as relevant.
    It does not need to be a stringent test. The goal is to filter out erroneous retrievals. \n
    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the qeustion. \n
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    Here is the retrieved document: \n\n {document} \n\n
    Here is the user question {question} \n <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    input_variables = ["question", "document"],
)

retrieval_grader = prompt | llm | JsonOutputParser()
question = "how to save llm cost?"
docs = retriever.invoke(question)
doc_txt = docs[1].page_content
print(retrieval_grader.invoke({'question': question, 'document':doc_txt}))

### Generate
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain_core.output_parsers import StrOutputParser

# Prompt
prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are an assistant for question-answering tasks.
    use the following pieces of retrieved context to answer the qeustion. If you don't know the answer, just say that you don't know. 
    use three sentences maximum and keep the answer concise <|eot_id|><|start_header_id|>user<|end_header_id|>
    Question: {question}
    context: {context}
    Answer: <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    input_variables=["question", "document"]
)

llm = ChatOllama(model = local_llm, temperature= 0)

# Post-processing
def format_docs(docs):
    return"\n\n".join(doc.page_content for doc in docs)

# Chain
rag_chain = prompt | llm | StrOutputParser()

# Run 
Question = "how to save llm cost?"
docs = retriever.invoke(question)
generation = rag_chain.invoke({"context": docs, "question":question})
print(generation)

### Web Search

os.environ['TAVILY_API_KEY'] = 'xxxxx'

from langchain_community.tools.tavily_search import TavilySearchResults
web_search_tool = TavilySearchResults(k=3)

### Halluination Grader

prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a grader assessing whether an answer is
    grounded in / supporated by a set of facts. Give a binary score 'yes' or 'no' to indicate wether the answer is grounded 
    in / supported by a set of facts. provide the binary score as a JSON with a single key 'score' and no preamble or explanation.
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    Here are the facts:
    \n ------ \n
    {documents}
    \n ------ \n
    Here is the answer: {generation} <|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    input_variables=["question", "document"],
)

hallucination_grader = prompt | llm | JsonOutputParser()
hallucination_grader.invoke({"documents": docs, "generation":generation})

from typing_extensions import TypedDict
from typing import List

### State

class GraphState(TypedDict):
    """represent the state of oru graph
    Attributes:
        question: question
        generation: LLM generation
        web_search: whether to add search
        documents: list of documents
    """
    question: str
    generation: str
    web_search: str
    documents: List[str]

from langchain.schema import Document

### Nodes

def retrieve(state):
    """
    Retrieve documents from vectorstore
    
    Args:
        stat(dict): The current graph state
    
    Returns:
        state (dict): New key added to state, docuemnts, that contains retrieved documents
    """
    print("---RETRIEVE---")
    question = state["question"]
    documents = state["documents"]

    # Retrieval
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}

def grade_documents(state):
    """
    Determines whether the retrieved documents are relevant to the qeustion
    If any docuemnt is not relevant, we weill set a flag to run web search
    
    Args:
        state (dict): The current graph state
        
    Returns: 
        state (dict): Filtered out irrelevant documents and updated web_search state
    
    """
    print("---CHECK DOCUMENT RELEVANCE TO QEUSTION---")
    question = state["qusetion"]
    documents = state["documents"]

    # Score each doc
    filtered_docs = []
    web_search = "No"
    for d in documents:
        score = retrieval_grader.invoke({"question": question, "document": d.page_content})
        grade = score['score']
        # Document relevant
        if grade.lower() == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(d)
        # Document not relevant
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            # We do not include the document in filtered_docs
            # We set a flag to indicate that we want to run web search
            web_search = "Yes"
            continue
    return {"documents": documents, "question": question, "generation": generation}

def genearte(state):
    """
    Generate answer using RAG on retrieved documents
    
    Arg:
        State (dict): the current graph state
        
    Returns:
        state (dict): New Key added to sate, generation, taht contains LLM generatiohn
    
    """
    print("---CHECK DOCUMENT RELEVANCE TO QEUSTION---")
    question = state["qusetion"]
    documents = state["documents"]

    # RAG generation
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}

def web_search(state):
    """
    web serach based on the qeustion
    
    Arg:
        State (dict): The current graph state
        
    Returns:
        state (dict): Appended web restults to docuemnts
    """

    print("---WEB SERACH---")
    question = state["qusetion"]
    documents = state["documents"]

    # Web search
    docs = web_search_tool.invoke({"query": question})
    web_results = "\n".join([d["content"] for d in docs])
    web_resutls = Document(page_content=web_results)
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    return {"docuemnts": documents, "question": question}

### Conditional edge

