                                 SPEECH RECOGNITION

This is a simple web-based **Speech Recognition** app built with **Streamlit** and the **Google Speech-to-Text API**.  
Users can upload `.mp3` or `.wav` audio files, and the app will transcribe the spoken content into text.

---

# FEATURES:

-  Upload `.mp3` or `.wav` audio files  
-  Automatic speech recognition using `speech_recognition`  
-  MP3 to WAV conversion using `pydub`  
-  Google Web Speech API for transcription  
-  Clean UI with custom CSS

---

# SCREENSHOTS:

![APP PREVIEW](screenshots/OUTPUT%201.png)

---

## 📂 FILE STRUCTURE

```
speech-recognition-app/
├── app.py
├── style.css
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    └── OUTPUT 1.png
```


#  HOW TO RUN:

1. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
   streamlit run app.py

---

# HOW IT WORKS:

1. Upload a `.mp3` or `.wav` audio file  
2. If needed, the app converts MP3 to WAV using `pydub`  
3. The audio is transcribed using Google’s Speech-to-Text API  
4. The transcribed text is displayed on the screen  
5. Errors or unclear audio are handled gracefully

---
