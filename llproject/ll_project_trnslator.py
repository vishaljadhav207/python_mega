import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
from tempfile import NamedTemporaryFile
from openai import OpenAI

# Configure OpenRouter API
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"  # Replace with your OpenRouter key
)

# Function: Recognize Speech
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak something...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        st.error("Could not understand audio.")
    except sr.RequestError:
        st.error("Could not request results from Speech API.")
    return ""

# Function: Translate using LLM via OpenRouter
def translate_with_llm(text, target_language):
    prompt = f"Translate this to {target_language}:\n\n{text}"

    try:
        response = client.chat.completions.create(
            model="nousresearch/deephermes-3-mistral-24b-preview:free",
            messages=[
                {"role": "system", "content": "You are a professional language translator."},
                {"role": "user", "content": prompt}
            ],
            extra_headers={
                "HTTP-Referer": "http://localhost",  # Optional: replace with your real app URL
                "X-Title": "LL Translator"
            }
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Translation failed: {e}")
        return ""

# Function: Text-to-Speech
def speak_text(text, lang_code="en"):
    try:
        tts = gTTS(text=text, lang=lang_code)
        with NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")
    except Exception as e:
        st.error(f"Text-to-Speech failed: {e}")

# Streamlit App UI
st.set_page_config(page_title="LL Translator", layout="centered")
st.title("🌐 LL Translator - Real-Time LLM-Based Language Translator")

input_mode = st.radio("Choose Input Mode:", ("Text", "Voice"))

input_text = ""
if input_mode == "Text":
    input_text = st.text_area("Enter the text to translate:")
else:
    if st.button("🎤 Start Recording"):
        input_text = recognize_speech_from_mic()
        if input_text.strip():
            st.success(f"You said: {input_text}")
        else:
            st.warning("❗ No speech recognized. Please try again.")

target_lang = st.selectbox("Choose target language:", ["Spanish", "French", "German", "Hindi", "Chinese", "Japanese"])

lang_map = {
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Japanese": "ja"
}

if st.button("🌍 Translate"):
    if input_text:
        with st.spinner("Translating..."):
            translated_text = translate_with_llm(input_text, target_lang)
            if translated_text:
                st.success("Translation complete!")
                st.text_area("Translated Text:", value=translated_text, height=100)

                if st.button("🔊 Play Translation"):
                    speak_text(translated_text, lang_code=lang_map.get(target_lang, "en"))
    else:
        st.warning("Please enter or speak some text to translate.")
