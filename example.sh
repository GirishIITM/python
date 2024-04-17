#!/bin/bash

API_KEY="AIzaSyBivcm38kKb7Ks79KGF7PvuXD8rtNoyofg"

curl \
  -X POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.0-pro-001:generateContent?key=${API_KEY} \
  -H 'Content-Type: application/json' \
  -d @<(echo '{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "hi"
        }
      ]
    },
    {
      "role": "model",
      "parts": [
        {
          "text": "Hello!  How can I help you today?"
        }
      ]
    },
    {
      "role": "user",
      "parts": [
        {
          "text": "write a py script to use gemini api"
        }
      ]
    }
  ],
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
}')