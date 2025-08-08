import requests

def chat_with_ollama(prompt, model='gemma3:1b'):
    url = 'http://localhost:11434/api/generate'
    data = {
        'model': model,
        'prompt': prompt,
        'stream': False  # Set to True for streaming responses
    }

    response = requests.post(url, json=data)
    return response.json()['response']

# Example usage
reply = chat_with_ollama("What is the capital of India?")
print(reply)
