import os
from smolagents import OpenAIServerModel

model = OpenAIServerModel(
    model_id="llama-3.2-3b-instruct",
    api_base="http://localhost:1234/v1", # Leave this blank to query OpenAI servers.
    api_key="dummy", # Switch to the API key for the server you're targeting.
)

from smolagents import CodeAgent, DuckDuckGoSearchTool

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)