from huggingface_hub import login
import os
api_key = os.environ["HF_API_KEY"] 
login(token=api_key)

from smolagents import CodeAgent, WebSearchTool, InferenceClientModel

model = InferenceClientModel()
agent = CodeAgent(tools=[WebSearchTool()], model=model, stream_outputs=True)

result = agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
print(result)