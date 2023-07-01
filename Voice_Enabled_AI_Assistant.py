import openai
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os
import json
from dotenv import load_dotenv, find_dotenv
import tempfile
from pocketsphinx import LiveSpeech
import wave
import uuid

load_dotenv(find_dotenv())

# Initialize the recognizer
r = sr.Recognizer()

# Define the wake word and the commands to disable/enable wake word mode
WAKE_WORD = "oracle"
DISABLE_WAKE_WORD_COMMAND = "deactivate"
ENABLE_WAKE_WORD_COMMAND = "activate"

# Initialize a variable to keep track of whether the bot is in wake word mode
wake_word_mode = True

# Function to listen for the wake word
def listen_for_wake_word():
    print("Listening for wake word..." if wake_word_mode else "Listening for activate command...")
    for phrase in LiveSpeech(): 
        if WAKE_WORD in str(phrase) and wake_word_mode:
            print("Heard wake word!")
            return True
        elif ENABLE_WAKE_WORD_COMMAND in str(phrase) and not wake_word_mode:
            print("Heard activate command!")
            return True
    return False

def listen(lang='en-US'):
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        # Save audio to a .wav file
        wav_data = audio.get_wav_data()
        with open(f"{uuid.uuid4()}.wav", "wb") as f:
            f.write(wav_data)
        try:
            text = r.recognize_google(audio, language=lang)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

def speak(text, lang='en'):
    temp = tempfile.NamedTemporaryFile(delete=True)
    temp.close()
    tts = gTTS(text=text, lang=lang)
    tts.save(temp.name)
    audio = AudioSegment.from_file(temp.name)
    # Save a copy of the bot's audio output
    bot_audio_file_name = f"bot_{uuid.uuid4()}.wav"
    audio.export(bot_audio_file_name, format="wav")
    play(audio)
    os.remove(temp.name)

def get_response(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if not openai.api_key:
        print("Missing OpenAI API Key")
        return None
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60
    )
    return response.choices[0].text.strip()

def store_conversation(prompt, response):
    data = []
    if os.path.isfile('conversation.json'):
        with open('conversation.json', 'r') as f:
            data = json.load(f)
    data.append({
        'Heard': prompt,
        'Response': response,
    })
    with open('conversation.json', 'w') as f:
        json.dump(data, f, indent=4)

while True:
    if wake_word_mode:
        if listen_for_wake_word():
            prompt = listen()
            if prompt is not None:
                print("Heard:", prompt)
                if prompt.lower() == DISABLE_WAKE_WORD_COMMAND:
                    wake_word_mode = False
                    print("Wake word mode disabled.")
                    continue
                response = get_response(prompt)
                if response is not None:
                    print("Response:", response)
                    speak(response)
                    store_conversation(prompt, response)
    else:
        prompt = listen()
        if prompt is not None:
            print("Heard:", prompt)
            if prompt.lower() == ENABLE_WAKE_WORD_COMMAND:
                wake_word_mode = True
                print("Wake word mode enabled.")
                continue
            response = get_response(prompt)
            if response is not None:
                print("Response:", response)
                speak(response)
                store_conversation(prompt, response)
