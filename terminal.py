history=[]

while True:
    query=input("You:")

    response=chain.invoke(
        {
            "history":history,
            "query":query
        }
    )

history.append(HumanMessage(content=query))
history.append(AIMessage(content=response.answer))