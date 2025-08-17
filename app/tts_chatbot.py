import io
from openai import OpenAI
from . import config
class TTSChatbot:
    def __init__(self, system_prompt="You are a helpful AI assistant."):
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)
        self.conversation_history = [{"role": "system", "content": system_prompt}]

    def chat(self, user_input: str) -> str:
        self.conversation_history.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model=config.GPT_MODEL,
            messages=self.conversation_history
        )
        reply = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": reply})
        return reply

    def tts(self, text: str, voice: str = config.DEFAULT_VOICE) -> bytes:
        """Return audio bytes from TTS."""
        audio_response = self.client.audio.speech.create(
            model=config.TTS_MODEL,
            voice=voice,
            input=text
        )
        return audio_response.content



