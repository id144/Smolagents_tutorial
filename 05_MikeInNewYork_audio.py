from smolagents import CodeAgent, InferenceClientModel

model_id = "meta-llama/Llama-3.3-70B-Instruct" 
model = InferenceClientModel(model_id=model_id)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Why does Mike not know many people in New York?",
    additional_args={"mp3_sound_file_url":'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/recording.mp3'}
)