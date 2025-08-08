import requests
import json

def get_answer(user_query, model='gemma3:1b'):
    url = 'http://localhost:11434/api/generate'
    system_prompt = (
        "You are MedBot, a clinical AI assistant. Answer medical questions clearly and precisely.\n\n"
        f"Instruction: Answer in 2–3 sentences using medically accurate terminology. Avoid unnecessary elaboration.\n"
        f"Patient: {user_query}\n"
        "MedBot:"
    )
    data = {
        'model': model,
        'prompt': system_prompt,
        'stream': True  # Set to True for streaming responses
    }

    full_response = ""
    with requests.post(url, json=data, stream=True) as response:
        for line in response.iter_lines():
            if line:
                try:
                    obj = json.loads(line.decode('utf-8'))
                    if "response" in obj:
                        print(obj["response"], end='', flush=True)
                        full_response += obj["response"]
                except json.JSONDecodeError as e:
                    print(f"⚠️ Decode error: {e}")

    return full_response
# Example usage
#reply = chat_with_ollama("What is the capital of India?")
#print(reply)




