from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
import os

login(os.environ['HUGGINGFACE_HUB_TOKEN'])

# model_name = "mistralai/Mistral-7B-v0.1"
# model_name = "tiiuae/falcon-7b"
# model_name = "gpt2"
model_name = "openai-community/gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./hf_model/")
tokenizer.save_pretrained("./hf_model/")