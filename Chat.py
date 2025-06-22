import ollama
import json

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Why is the sky blue?"},
    ],
    
)
#print the response from ollama.chat
print("Response:", response) # prints payload with metadata of the response
print("Response content:", response["message"]["content"]) #prints the content only, no metadata
