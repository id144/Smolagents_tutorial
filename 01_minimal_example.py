from smolagents import CodeAgent, InferenceClientModel
import os

api_key = os.environ["HF_API_KEY"] 
model = InferenceClientModel(api_key=api_key) # Uses a default model

# Create an agent with no tools
agent = CodeAgent(tools=[], model=model)

# Run the agent with a task
result = agent.run("Calculate the sum of numbers from 1 to 10")
print(result)