import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os
import threading

def record_and_translate():
    r = sr.Recognizer()
    translator = google_translator()

    with sr.Microphone() as source:
        print("Speak Now!...")
        audio = r.listen(source, timeout=10)  # Record for 10 seconds
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if speech_text.lower() == "exit":
                return

            translated_text = translator.translate(speech_text, lang_tgt="fr")
            print(translated_text)

            voice = gTTS(translated_text, lang="fr")
            voice.save("voice.mp3")
            playsound("voice.mp3")
            os.remove("voice.mp3")
        except sr.UnknownValueError:
            print("Could Not Understand...")
        except sr.RequestError:
            print("Could not request result from Google...")

while True:
    input("Press Enter to start recording for 10 seconds...")
    recording_thread = threading.Thread(target=record_and_translate)
    recording_thread.start()
    recording_thread.join()  # Wait for the recording and translation to finish

    continue_input = input("Do you want to continue? (y/n): ")
    if continue_input.lower() != "y":
        break
