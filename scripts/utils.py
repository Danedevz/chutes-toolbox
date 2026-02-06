import base64
import io
from PIL import Image

def pil_to_base64(img: Image.Image) -> str:
    """Convert a PIL Image to a base64‑encoded PNG string."""
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("utf-8")
