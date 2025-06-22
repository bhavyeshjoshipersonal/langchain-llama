import ollama

response = ollama.list()
print("Available Models:", response)