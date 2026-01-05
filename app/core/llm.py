from langchain_groq import ChatGroq
from fastapi import HTTPException
import os
from dotenv import load_dotenv
load_dotenv()


def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="LLM service not configured"
        )

    try:
        return ChatGroq(
            model_name="llama-3.1-8b-instant",
            temperature=0
        )
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Failed to initialize LLM service"
        )
