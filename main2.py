import os
import subprocess

def convert_to_wav(input_file, output_file):
    # Check if the output directory exists, if not, create it
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Path to the FFmpeg executable
    ffmpeg_path = r"C:\Hack\ffmpeg\ffmpeg-2.2.2-win64-static\bin\ffmpeg.exe"

    # Run FFmpeg to convert the audio file to WAV format
    try:
        subprocess.run([ffmpeg_path, '-i', input_file, '-acodec', 'pcm_s16le', '-ac', '1', '-ar', '16000', output_file])
        return output_file  # Return the converted file path
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        return None  # Indicate failure

input_file = r"C:\Users\adida\Documents\Dell\6002335182.mp3\_6002335182.mp3"
output_dir = r"C:\Users\adida\Documents\wav_files"
wav_file = convert_to_wav(input_file, os.path.join(output_dir, os.path.splitext(os.path.basename(input_file))[0] + ".wav"))

if wav_file:  # Check if conversion was successful
    import speech_recognition as sr

    def transcribe_audio(wav_file):
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_file) as source:
            audio_data = recognizer.record(source)  # Read the entire audio file

        # Using recognizer to convert speech to text
        try:
            transcription = recognizer.recognize_google(audio_data)
            return transcription
        except sr.UnknownValueError:
            return "Speech recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

    transcription = transcribe_audio(wav_file)
    print("Transcription:", transcription)
else:
    print("Conversion failed. Exiting.")
