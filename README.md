# SPEECH RECOGNITION SYSTEM        

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : ARVA ARAVINDA SAI

*INTERN ID*: CODF219

*DOMAIN*:ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH


                                            SPEECH RECOGNITION

This is a simple web-based **Speech Recognition** app built with **Streamlit** and the **Google Speech-to-Text API**.  
Users can upload `.mp3` or `.wav` audio files, and the app will transcribe the spoken content into text.

---

# FEATURES:

-  Upload `.mp3` or `.wav` audio files  
-  Automatic speech recognition using `speech_recognition`  
-  MP3 to WAV conversion using `pydub`  
-  Google Web Speech API for transcription  
-  Clean UI with CSS Styles

---

# APP PREVIEW:

![APP PREVIEW](screenshots/OUTPUT%201.png)
# WORKING:
![OUTPUT 2](https://github.com/user-attachments/assets/6e8bdd9f-374f-4986-9aa5-a3dc97330dc7)

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

1. Clone this repository:
   git clone https://github.com/Aravinda-Sai10/Speech-Recognition.git
   cd Speech-Recognition

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   streamlit run app.py

---

# HOW IT WORKS:

1. Upload a `.mp3` or `.wav` audio file  
2. If needed, the app converts MP3 to WAV using `pydub`  
3. The audio is transcribed using Google’s Speech-to-Text API  
4. The transcribed text is displayed on the screen  
5. Errors or unclear audio are handled gracefully

---
# USES:
1.**Convert Speech to Text**:
      Quickly transcribe audio files into readable text using Google's speech recognition.

 2.**Assistive Tool for Students & Professionals**:
      Turn lectures, meetings, or voice memos into text notes.

3.**Accessibility Enhancement**:
     Helps hearing-impaired users understand spoken content.

4.**Prototype for Speech AI Projects**:
    A solid base to build more advanced speech-to-text or voice assistant systems.
