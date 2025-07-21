from smolagents import CodeAgent, InferenceClientModel
import os
model_id = "meta-llama/Llama-3.3-70B-Instruct"

api_key = os.environ["HF_API_KEY"] 
model = InferenceClientModel()
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

result = agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)

print(result)