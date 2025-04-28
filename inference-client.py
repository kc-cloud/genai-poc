import streamlit as st
import requests
import re

# Set your inference server URL
INFERENCE_SERVER_URL = "http://localhost:8000/generate"

# Streamlit page config
st.set_page_config(page_title="GPT-2 Text Generator", page_icon="📝", layout="centered")

st.title("📝 GPT-2 Text Generator")
st.subheader("Enter a prompt and let the model complete it!")

# User input
prompt = st.text_area("Prompt:", height=150)
max_tokens = st.slider("Max tokens to generate:", min_value=10, max_value=1024, value=50)

# Button to generate
if st.button("Generate Text"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Generating..."):
            payload = {
                "prompt": prompt,
                "max_tokens": max_tokens
            }
            try:
                response = requests.post(INFERENCE_SERVER_URL, json=payload)
                if response.status_code == 200:
                    generated_text = response.json()["generated_text"]
                    st.success("Generated Text:")
                    match = re.search(r'([.!?])', generated_text[len(prompt):])
                    if match:
                        end_idx = match.end() + len(prompt)
                        final_text = generated_text[:end_idx]
                    else:
                        final_text = generated_text                    
                    st.write(generated_text)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Failed to connect to server: {e}")
