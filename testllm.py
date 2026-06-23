from llm import llm

print("Invoking Gemini...")

response = llm.invoke("Hello")

print(response.content)