#write code to import ollama
import ollama
import json 

#write code to show the model information using ollama.show
response = ollama.show(model="llama3.2")
print("Model Information:", response)
