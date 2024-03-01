# STT
import speech_recognition as sr

def transcribe_audio(wav_file):
    recognizer = sr.Recognizer()
   
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file
   
    # Use the recognizer to convert speech to text
    try:
        transcription = recognizer.recognize_google(audio_data)
        return transcription
    except sr.UnknownValueError:
        return "Speech recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

transcription = transcribe_audio(output_file)
print("Transcription:", transcription)
