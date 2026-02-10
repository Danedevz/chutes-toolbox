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

def handle_template(value):
    is_custom = value == "Custom"
    if not is_custom:
        return gr.update(interactive=is_custom, placeholder="Change template to \"Custom\" to define custom prompts")
    return gr.update(interactive=is_custom, placeholder="")


with gr.Blocks() as demo:
    gr.Markdown("""
# Chutes Toolbox
        
        """)
    #Captioning Tab
    with gr.Tab("Captioning"):
        gr.Textbox(label="API Token")
        Template_Dropdown = gr.Dropdown(
            ["Custom", "Stable Diffusion", "Danbooru"], 
            value="Custom", 
            label="Template prompt",
        )
        Prompt_Textbox = gr.Textbox(label="Prompt", interactive=True)
        Template_Dropdown.change(handle_template, inputs=Template_Dropdown, outputs=Prompt_Textbox)

    with gr.Tab("Edit"):
        api_token_edit = gr.Textbox(label="API token", type="password")
        seed = gr.Number(label="seed", value=None)
        width = gr.Number(label="width", value=1024, info="pixels")
        height = gr.Number(label="height", value=1024, info="pixels")
        prompt = gr.Textbox(label="prompt")
        image_input = gr.Image(label="image", type="pil")
        cfg = gr.Slider(label="true cfg scale", step=1, value=4, maximum=10)
        steps = gr.Slider(label="steps", step=1, value=40)
        negative_prompt = gr.Textbox(label="negative prompt")
        run_btn = gr.Button("Run")
        result = gr.Image(label="result", type="filepath", interactive=False, format="jpeg")
        run_btn.click(
            fn=handle_edit,
            inputs=[
                api_token_edit, seed, width, height,
                prompt, image_input, cfg, steps, negative_prompt,
            ],
            outputs=result,
        )

generation = gr.Interface(
    fn=lambda fn: "None",
    inputs=[
        gr.Text("Placeholder")
    ],
    outputs=gr.Textbox(visible=False),
    api_name="predict"
)

#demo = gr.TabbedInterface([captioning, generation, image_edit], ["Captioning", "Generation", "Edit"])

if __name__ == "__main__":
    demo.launch()
