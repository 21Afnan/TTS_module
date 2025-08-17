from fastapi import FastAPI, Query, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
import io
from .tts_chatbot import TTSChatbot
from . import config
app = FastAPI(title="TTS Module API")
# Allow all origins (for testing / website embedding)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Initialize chatbot
bot = TTSChatbot()
@app.get("/")
def home():
     return FileResponse("index.html")

@app.post("/chat")
def chat(payload: dict = Body(...)):
    message = payload.get("message", "").strip()
    if not message:
        return JSONResponse({"error": "No message provided"}, status_code=400)
    try:
        reply = bot.chat(message)
        return {"reply": reply}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

@app.get("/tts")
def tts(text: str = Query(..., description="Text to convert to speech"),
        voice: str = Query(config.DEFAULT_VOICE, description="Voice to use")):
    """
    Convert text to speech and return raw audio bytes.
    """
    try:
        audio_bytes = bot.tts(text, voice)
        if not audio_bytes:
            return {"error": "No audio generated"}  # only return JSON on error

        # Return bytes as audio/mpeg so frontend can play directly
        return StreamingResponse(
            io.BytesIO(audio_bytes),
            media_type="audio/mpeg",
            headers={"Content-Disposition": "inline; filename=tts.mp3"}
        )
    except Exception as e:
        return {"error": str(e)}