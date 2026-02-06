import requests
import io
import gradio as gr
from PIL import Image
from scripts.config import API_URL

def fetch_edit_model(token: str, payload: dict) -> Image.Image:
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    try:
        response: requests.Response = requests.post(
            url=API_URL,
            headers=headers,
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            raise gr.Error("Unauthorized – check your API token.")
        raise gr.Error(f"HTTP {e.response.status_code}: {e.response.text[:300]}")
    except requests.exceptions.RequestException as e:
        raise gr.Error(str(e))

    return Image.open(io.BytesIO(response.content))
