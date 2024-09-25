from os import environ
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = environ['OPENAI_API_KEY']

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI


# Create an llm object to use for the QueryEngine and the ReActAgent
llm = OpenAI(model="gpt-3")

from openinference.instrumentation.llama_index import LlamaIndexInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk import trace as trace_sdk
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

import phoenix as px
session = px.launch_app()

endpoint = "http://127.0.0.1:6006/v1/traces"  # Phoenix receiver address

tracer_provider = trace_sdk.TracerProvider()
tracer_provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter(endpoint)))

LlamaIndexInstrumentor().instrument(tracer_provider=tracer_provider)

try:
    storage_context = StorageContext.from_defaults(
        persist_dir="/Users/taypham/Documents/GitHub/Python/Projects/OpenAI/Storage"
    )
    lyft_index = load_index_from_storage(storage_context)

    storage_context = StorageContext.from_defaults(
        persist_dir="/Users/taypham/Documents/GitHub/Python/Projects/OpenAI/Storage"
    )
    uber_index = load_index_from_storage(storage_context)

    index_loaded = True
except:
    index_loaded = False

if not index_loaded:
    # load data
    lyft_docs = SimpleDirectoryReader(
        input_files=["/Users/taypham/Documents/GitHub/Python/Projects/OpenAI/Storage/lyft_2021.pdf"]
    ).load_data()
    uber_docs = SimpleDirectoryReader(
        input_files=["/Users/taypham/Documents/GitHub/Python/Projects/OpenAI/Storage/uber_2021.pdf"]
    ).load_data()

    # build index
    lyft_index = VectorStoreIndex.from_documents(lyft_docs, show_progress=True)
    uber_index = VectorStoreIndex.from_documents(uber_docs, swow_progress=True)

    # persist index
    lyft_index.storage_context.persist(persist_dir="/Users/taypham/Documents/GitHub/Python/Projects/OpenAI/Storage")
    uber_index.storage_context.persist(persist_dir="/Users/taypham/Documents/GitHub/Python/Projects/OpenAI/Storage")

lyft_engine = lyft_index.as_query_engine(similarity_top_k=3, llm=llm)
uber_engine = uber_index.as_query_engine(similarity_top_k=3, llm=llm)

query_engine_tools = [
    QueryEngineTool(
        query_engine=lyft_engine,
        metadata=ToolMetadata(
            name="lyft_10k",
            description=(
                "Provides information about Lyft financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
    QueryEngineTool(
        query_engine=uber_engine,
        metadata=ToolMetadata(
            name="uber_10k",
            description=(
                "Provides information about Uber financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    ),
]

agent = ReActAgent.from_tools(
    query_engine_tools,
    llm=llm,
    verbose=True,
    max_turns=10,
)

response = agent.chat("Who had more profit in 2021, Lyft or Uber?")
print(str(response))