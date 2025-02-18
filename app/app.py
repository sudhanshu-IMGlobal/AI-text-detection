from fastapi import FastAPI
from routes import detect
from middlewares.rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI(title="AI Text Detector API", version="1.0.0")

# Include middleware
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# Register routes
app.include_router(detect.router)

@app.get("/")
async def root():
    return {"message": "AI Text Detector API is running!"}
