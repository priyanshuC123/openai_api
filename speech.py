import pyttsx3
import speech_recognition as sr
import openai
import env
# openai key
openai.api_key = env.OPEN_AI_KEY

# initialize speech engine
engine = pyttsx3.init()


def speak(word):
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 0.8)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(str(word))
    engine.runAndWait()
    engine.stop()


# Initialize Speech Recognizer
rec = sr.Recognizer()
speak('hello Sir, I am listening for your command')
with sr.Microphone() as source:
    audio = rec.listen(source)
    speak('I am computing an answer for your request. i will be done soon')

text = rec.recognize_google_cloud(audio)

# discussion = openai.chat.completions.create(
#     prompt=text,
#     engine='text-davinci-002',
#     max_tokens=1000,
# )

response = openai.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": text},
  ]
)

answer=response.choices[0].message.content

if answer:
    speak(answer)