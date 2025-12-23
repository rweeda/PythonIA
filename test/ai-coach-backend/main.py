from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (OK for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HintRequest(BaseModel):
    task_md: str
    language: str
    code: str
    output: str
    level: str = "beginner"
    mode: str = "hint"

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/api/hint")
def hint(req: HintRequest):
    prompt = f"""
You are a programming tutor.

Student level: {req.level}
Language: {req.language}

TASK (markdown):
{req.task_md}

STUDENT CODE:
{req.code}

PROGRAM OUTPUT / ERROR:
{req.output}

RULES:
- Give hints only
- Do NOT provide the full solution
- Be concise
"""

    r = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
        params={"key": GEMINI_API_KEY},
        json={
            "contents": [{
                "role": "user",
                "parts": [{"text": prompt}]
            }]
        }
    )

    data = r.json()
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    return {"text": text}
