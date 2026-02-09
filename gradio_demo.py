import gradio as gr

# Simple function to add two numbers
def add_numbers(a, b):
    return a + b

# Create the interface
demo = gr.Interface(
    fn=add_numbers,
    inputs=["number", "number"],  # two number inputs
    outputs="number"             # one number output
)

# Launch the app
demo.launch(server_name="0.0.0.0", server_port=7860)
