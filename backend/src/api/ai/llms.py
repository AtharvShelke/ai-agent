import os
from langchain_openai import OpenAI, ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()  # only needed if using a .env file

# Load environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GOOGLE_GENAI_MODEL_NAME = os.getenv("GOOGLE_GENAI_MODEL_NAME")
GOOGLE_GENAI_BASE_URL = os.getenv("GOOGLE_GENAI_BASE_URL")

# DEBUG print
print("GEMINI_API_KEY:", bool(GEMINI_API_KEY))  # True if set
print("GOOGLE_GENAI_MODEL_NAME:", GOOGLE_GENAI_MODEL_NAME)

# Check for required variables
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is not set in environment.")
if not GOOGLE_GENAI_MODEL_NAME:
    raise ValueError("❌ GOOGLE_GENAI_MODEL_NAME is not set in environment.")



# Construct params


def get_llm():
    openai_param = {
    "model": GOOGLE_GENAI_MODEL_NAME,
    "api_key": GEMINI_API_KEY,
    }
    if GOOGLE_GENAI_BASE_URL:
        openai_param["base_url"] = GOOGLE_GENAI_BASE_URL
    """Instantiate and return the LLM."""
    return ChatOpenAI(**openai_param)


