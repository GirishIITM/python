import json
from typing import Dict, List, Union, Any

import requests


def gimini_chat(msg: str) -> Dict[str, Union[str, Dict[str, Any]]]:
    API_KEY = "AIzaSyBivcm38kKb7Ks79KGF7PvuXD8rtNoyofg"  # Replace with your actual API key
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.0-pro-001:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}

    try:
        data: Dict[str, Union[Dict[str, str], List]] = {
            "contents": [],
            "generationConfig": {
                "temperature": 0.9,
                "topK": 1,
                "topP": 1,
                "maxOutputTokens": 2048,
                "stopSequences": []
            },
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                }
            ]
        }

        user_message = {
            "role": "user",
            "parts": [
                {
                    "text": msg
                }
            ]
        }
        data["contents"].append(user_message)

        res: Dict[str, Any] = requests.post(url, headers=headers, json=data).json()
        text = res["candidates"][0]["content"]["parts"][0]["text"]
        data['contents'].append({
            "role": "model",
            "parts": [
                {
                    "text": text
                }
            ]
        })
        print(json.dumps(text, indent=4))
        return {
            'response': text,
            'error': None
        }

    except Exception as err:
        print(err, 'error occured in gimini chat function')
        return {
            'error': str(err)
        }


# Example usage
response = gimini_chat("write a Python script")
if response.get('error'):
    print("Error:", response['error'])
else:
    print("Bard's Response:", response['response'])
