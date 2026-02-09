# Import packages
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
import gradio as gr

# Set up credentials and model
credentials = Credentials(url="https://us-south.ml.cloud.ibm.com")
model_id = "meta-llama/llama-3-2-11b-vision-instruct"
project_id = "skills-network"

# Initialize the model (constructor only takes model_id, credentials, project_id)
model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id
)

# Function to generate response
def generate_response(prompt_txt):
    messages = [{"role": "user", "content": [{"type": "text", "text": prompt_txt}]}]
    # Set parameters like temperature and max_output_tokens here
    response = model.chat(
        messages=messages,
        temperature=0.1,
        max_output_tokens=256
    )
    return response['choices'][0]['message']['content']

# Gradio interface
chat_app = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label="Your Question", placeholder="Type something..."),
    outputs=gr.Textbox(label="Chatbot Answer"),
    title="Watsonx.ai Chatbot",
    description="Ask a question and get a response from Watsonx.ai's LLM"
)

# Launch the app
chat_app.launch()
