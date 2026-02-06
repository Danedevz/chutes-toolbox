import gradio as gr
from scripts.api_client import fetch_edit_model
from scripts.utils import pil_to_base64
from PIL import Image


def handle_edit(token: str, seed: int | None, width: int, height: int, prompt: str, image: Image.Image, cfg: int, steps: int, negative_prompt: str = ""):
    # Convert PIL Image to base64 string
    image_b64s = [pil_to_base64(image)]
    payload = {
        "seed": seed,
        "width": width,
        "height": height,
        "prompt": prompt,
        "image_b64s": [image_b64s],
        "true_cfg_scale": cfg,
        "num_inference_steps": steps,
        "negative_prompt": negative_prompt,
    }
    return fetch_edit_model(token=token, payload=payload)

captioning = gr.Interface(
    fn=lambda fn: "None",
    inputs=[
        gr.Text("Placeholder")
    ],
    outputs=gr.Textbox(visible=False),
    api_name="predict"
)

generation = gr.Interface(
    fn=lambda fn: "None",
    inputs=[
        gr.Text("Placeholder")
    ],
    outputs=gr.Textbox(visible=False),
    api_name="predict"
)

image_edit = gr.Interface(
    fn=handle_edit,
    inputs=[
        gr.Textbox(label="API token", type="password"),
        gr.Number(label="seed", value=None),
        gr.Number(label="width", value=1024, info="pixels"),
        gr.Number(label="height", value=1024, info="pixels"),
        gr.Textbox(label="prompt"),
        gr.Image(label="image", type="pil"),
        gr.Slider(label="true cfg scale", step=1, value=4, maximum=10),
        gr.Slider(label="steps", step=1, value=40),
        gr.Textbox(label="negative prompt"),
    ],
    outputs=gr.Image(label="result", type="filepath", interactive=False, format="jpeg"),
    api_name="predict",
)

demo = gr.TabbedInterface([captioning, generation, image_edit], ["Captioning", "Generation", "Edit"])

if __name__ == "__main__":
    demo.launch()
