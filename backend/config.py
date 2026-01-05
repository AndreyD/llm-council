"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Host URL for CORS (e.g., "http://46.224.197.208" or "https://example.com")
# If not set, only localhost origins are allowed
HOST_URL = os.getenv("HOST_URL")

# Council members - list of OpenRouter model identifiers
# See available models at: https://openrouter.ai/models
# Free models have ":free" suffix (lower quality but no cost)
COUNCIL_MODELS = [
    "google/gemma-3-4b-it:free",
    "meta-llama/llama-3.2-3b-instruct:free",
    "qwen/qwen3-4b:free",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "google/gemma-3-4b-it:free"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
