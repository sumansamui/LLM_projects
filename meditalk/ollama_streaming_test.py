import requests
import json

def stream_response(prompt, model="gemma3:1b"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": True
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
stream_response("What is migraine?")
