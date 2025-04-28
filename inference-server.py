from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Load the GPT2 model
generator = pipeline("text-generation", model="./hf_model")

# Setup FastAPI app
app = FastAPI()

# Define the request schema
class GenerationRequest(BaseModel):
    prompt: str
    max_tokens: int = 50

# API route for text generation
@app.post("/generate")
async def generate_text(request: GenerationRequest):
    output = generator(request.prompt, max_length=request.max_tokens, do_sample=True)
    return {"generated_text": output[0]["generated_text"]}
