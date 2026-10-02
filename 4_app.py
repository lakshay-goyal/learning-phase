# MAKE SURE TO INSTALL LIBRARIES USING THE COMMAND
#pip install streamlit ollama Pillow

# Also make sure to download the model you are using , download it using Ollama


import streamlit as st
import ollama
from PIL import Image
import base64
import io

# ==============================
# CONFIG
# ==============================

MODEL_NAME = "gemma3:4b"  # or llava, qwen2.5-vl, etc.

# ==============================
# SYSTEM INSTRUCTION
# ==============================

SYSTEM_INSTRUCTION = """
You are a Visual AI Tutor and  with over 12 years of experience in processing images and task associated with images.

Identity & Persona:
- Job Title: Visual AI Tutor 
- Experience Level: 12+ years
- Communication Style: Professional, structured, educator-focused
- Key Values: accuracy, transparency, teaching by example

Task Constraints & Boundaries:
- Do NOT guess, fabricate, or hallucinate details.
- Do NOT infer sensitive attributes.
- Do NOT give legal, medical, or professional advice.
- Do NOT go off-topic or add assumptions.
- If something cannot be determined, explicitly say so.

Communication Style & Format:
- Clear, professional, beginner-friendly
- Simple language, minimal jargon
- Structured output using bullets or short sections
- No emojis, no slang, no casual tone
- Always tell joke at end after output is generated.

Context (Audience):
- Undergraduate students and early-career professionals
- Basic technical familiarity, new to system instructions
"""

# ==============================
# HELPERS
# ==============================

def image_to_base64(image: Image.Image) -> str:
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def run_ollama(user_prompt: str, image: Image.Image):
    img_b64 = image_to_base64(image)

    response = ollama.generate(
        model=MODEL_NAME,
        system=SYSTEM_INSTRUCTION,
        prompt=user_prompt,
        images=[img_b64],
    )

    return response["response"]


# ==============================
# STREAMLIT UI
# ==============================

st.set_page_config(page_title="System Instruction Demo", page_icon="🧠")
st.title("🧠 System Instruction Demonstration (Ollama)")

uploaded_image = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "webp"]
)

user_prompt = st.text_area(
    "Enter your prompt (this is the USER instruction)",
    placeholder="Example: Describe the scene and list visible objects."
)

if uploaded_image and user_prompt.strip():
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Generate Output"):
        with st.spinner("Running Ollama model..."):
            try:
                output = run_ollama(user_prompt, image)
                st.subheader("📋 Model Output")
                st.write(output)
            except Exception as e:
                st.error(str(e))
else:
    st.info("Upload an image and enter a prompt to continue.")
