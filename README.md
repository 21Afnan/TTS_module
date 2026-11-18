<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0B1A2E,50:1B66C8,100:2F80ED&height=190&section=header&text=TTS%20Module&fontSize=52&fontColor=FFFFFF&fontAlignY=36&desc=Text%20to%20speech%20for%20any%20chatbot%2C%20as%20a%20small%20API&descSize=16&descAlignY=58" width="100%" alt="TTS Module"/>

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/HTML%20%2F%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML and JS"/>
</p>

</div>

---

## Why it exists

A text chatbot becomes far easier to use when it can talk back. This module gives any chatbot a voice without the chatbot having to know anything about audio: the frontend sends text, the API returns an MP3 that the browser plays immediately.

It is one of three reusable voice modules I packaged during my Conversational AI internship at Prudential Solutions, where I evaluated and benchmarked GPT-based speech components for an enterprise HR chatbot. Its siblings are [STT_module](https://github.com/21Afnan/STT_module) (speech to text) and [STS_module](https://github.com/21Afnan/STS_module) (speech to speech).

## Features

- **Chat with memory:** replies come from an OpenAI chat model (`gpt-4o-mini`), and the conversation history is kept so follow-up questions make sense.
- **Natural speech:** any reply, or any text you send, is turned into audio with OpenAI's `gpt-4o-mini-tts` model, with the voice selectable per request (default `nova`).
- **Streams straight to the browser:** audio is returned as `audio/mpeg`, so an `<audio>` element can play it with no extra decoding.
- **Ready-made chat page:** `index.html` is a complete chat interface that calls the API and plays each reply aloud.
- **Easy to swap:** models and the default voice live in one place, `app/config.py`.

## API

| Method | Endpoint | Input | Returns |
|---|---|---|---|
| `GET` | `/` | | the chat web page |
| `POST` | `/chat` | `{"message": "Hello"}` | `{"reply": "..."}` |
| `GET` | `/tts` | `?text=Hello&voice=nova` | MP3 audio stream |

```
Browser chat page ──POST /chat──> TTSChatbot.chat()  ──> OpenAI chat model
        ▲                                  │
        └──── MP3 ◄── GET /tts ◄── TTSChatbot.tts() ──> OpenAI TTS model
```

## Run it

```bash
git clone https://github.com/21Afnan/TTS_module.git
cd TTS_module
python -m venv venv && venv\Scripts\activate      # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_key_here
```

Start the server and open `http://127.0.0.1:8000`:

```bash
uvicorn app.main:app --reload
```

## Project structure

```
TTS_module/
├── app/
│   ├── main.py           # FastAPI routes: page, /chat, /tts
│   ├── tts_chatbot.py    # TTSChatbot: chat with history + text to speech
│   ├── chat_service.py   # single-turn chat helper
│   ├── config.py         # API key, model names, default voice
│   └── index.html
├── index.html            # chat interface served at /
└── requirements.txt
```

## Tech stack

Python, FastAPI, Uvicorn, OpenAI Python SDK (chat and speech models), python-dotenv, HTML, CSS and JavaScript.

---

<div align="center">

**Afnan Shoukat**

<a href="mailto:afnanshoukat35@gmail.com"><img src="https://img.shields.io/badge/Email-afnanshoukat35%40gmail.com-2F80ED?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0B1A2E" alt="Email"/></a>
<a href="https://www.linkedin.com/in/afnanshoukat"><img src="https://img.shields.io/badge/LinkedIn-Afnan%20Shoukat-2F80ED?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0B1A2E" alt="LinkedIn"/></a>
<a href="https://github.com/21Afnan"><img src="https://img.shields.io/badge/GitHub-21Afnan-2F80ED?style=for-the-badge&logo=github&logoColor=white&labelColor=0B1A2E" alt="GitHub"/></a>

</div>
