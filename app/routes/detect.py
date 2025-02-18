from fastapi import APIRouter, Depends, HTTPException, Request
from models import TextRequest, AIResponse
from services.ai_detector import AIDetector
from middlewares.rate_limiter import limiter

router = APIRouter()

@router.post("/detect-ai", response_model=AIResponse)
@limiter.limit("5/minute")  # Limit 5 requests per minute per IP
async def detect(request: Request, text_data: TextRequest):
    """API endpoint to detect AI-generated text and return a confidence percentage."""
    if not text_data.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    confidence = await AIDetector.detect_ai_text(text_data.text)
    return AIResponse(ai_confidence=confidence)
