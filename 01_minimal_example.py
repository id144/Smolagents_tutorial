from smolagents import CodeAgent, InferenceClientModel
import os

model = InferenceClientModel() # Uses a default model

# Create an agent with no tools
agent = CodeAgent(tools=[], model=model)

# Run the agent with a task
result = agent.run("Calculate the sum of numbers from 1 to 10")
print(result)