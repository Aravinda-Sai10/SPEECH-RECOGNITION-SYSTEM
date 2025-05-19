# === Import necessary libraries ===
import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

# === Streamlit Page Configuration ===
st.set_page_config(page_title="🎙️ Speech Recognition", layout="centered")

# === CSS for styling ===
def load_css():
    css_file = "style.css"
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ CSS file not found.")

load_css()

# === Title and Description ===
st.markdown("<h1 class='main-title'>🎙️ Speech Recognition</h1>", unsafe_allow_html=True)
st.markdown("<p class='description'>Upload your audio file (.mp3 or .wav) and we'll transcribe it for you using Google's Speech-to-Text.</p>", unsafe_allow_html=True)

# === Audio File Upload ===
audio_file = st.file_uploader("📤 Upload MP3 or WAV", type=["mp3", "wav"])

# === Transcription Button ===
if st.button(" Transcribe File"):
    if audio_file:
        recognizer = sr.Recognizer()

        # Create a temporary WAV file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            if audio_file.type == "audio/mp3":
                audio = AudioSegment.from_file(audio_file, format="mp3")
            else:
                audio = AudioSegment.from_file(audio_file, format="wav")
            audio.export(tmp_file.name, format="wav")

            with sr.AudioFile(tmp_file.name) as source:
                audio_data = recognizer.record(source)
                try:
                    text = recognizer.recognize_google(audio_data)
                    st.markdown("<h3>📝 Transcription:</h3>", unsafe_allow_html=True)
                    st.success(text)
                except sr.UnknownValueError:
                    st.warning("🤔 Couldn't understand the audio.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please upload an audio file.")