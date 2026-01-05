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
COUNCIL_MODELS = [
    "openai/gpt-4o",
    "google/gemini-2.0-flash-001",
    "anthropic/claude-sonnet-4",
    "x-ai/grok-3",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "google/gemini-2.0-flash-001"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
