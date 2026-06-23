from chainbuilder import chain
print("chain imported successfully")


response = chain.invoke({
    "history": [],
    "query": "Tell me about Messi"
})

print(response)