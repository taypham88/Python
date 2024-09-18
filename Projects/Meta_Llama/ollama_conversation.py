import requests
import json

url = "http://localhost:11434/api/chat"


def connect_to_ollama_model(messages):
    data = {
        "model": "llama3",
        "messages": messages,  # Send all messages in the conversation
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["message"]["content"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def main():
    print("Welcome to the Ollama Model Interface!")
    print("Type 'exit' to quit the program.")

    conversation_history = []

    while True:
        prompt = input("Enter your prompt: ")
        if prompt.lower() == 'exit':
            break

        conversation_history.append({"role": "user", "content": prompt})

        response = connect_to_ollama_model(conversation_history)

        if response:
            conversation_history.append({"role": "assistant", "content": response})
            print(f"Model Response: {response}")
        else:
            print("No response received from the model.")

if __name__ == "__main__":
    main()