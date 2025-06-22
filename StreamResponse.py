import ollama
import json

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Why is the sky blue?"},
    ],
    stream=True,  # Enable streaming
)
#print the response from ollama.chat using streaming
for chunk in response:
    print (chunk["message"]["content"], end="",flush=True)  # prints each chunk of the response
