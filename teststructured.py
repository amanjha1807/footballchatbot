from llm import llm
from schema import FootballResponse

structured_llm = llm.with_structured_output(FootballResponse)

response = structured_llm.invoke("Tell me about Messi")

print(response)