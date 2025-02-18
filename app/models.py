from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class AIResponse(BaseModel):
    ai_confidence: int
