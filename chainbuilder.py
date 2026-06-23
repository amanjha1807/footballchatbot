print("1. Importing llm...")
from llm import llm

print("2. Importing prompt...")
from template import prompt

print("3. Importing schema...")
from schema import FootballResponse

print("4. Creating structured llm...")
structured_llm = llm.with_structured_output(FootballResponse)

print("5. Creating chain...")
chain = prompt | structured_llm

print("6. Chain created successfully!")