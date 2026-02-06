# Configuration constants for the Gradio project
# You can override the API URL via the CHUTES_API_URL environment variable.
import os

API_URL = os.getenv(
    "CHUTES_API_URL",
    "https://chutes-qwen-image-edit-2509.chutes.ai/generate",
)
