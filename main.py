from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

# Initialize FastAPI
app = FastAPI()

# Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Initialize Google Gemini API
API_KEY = "<API_KEY>"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Define request model
class UserInput(BaseModel):
    prompt: str

# Test Route
@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

# Gemini AI Chat API
@app.post("/chat")
def chat_with_gemini(data: UserInput):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(data.prompt)
    return {"response": response.text}

