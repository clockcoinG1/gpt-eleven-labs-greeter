import sys
from elevenlabs import generate, stream, set_api_key, VoiceSettings
import os
import openai
import datetime

settings = VoiceSettings(stability=0.21, similarity_boost=0.1, style=0.1, use_speaker_boost=True, speaking_rate=0.5, pitch=0.24, volume=0.99)
openai.api_key = os.getenv("OPENAI_API_KEY")
eleven_labs_api_key = os.getenv("ELEVEN_LABS_API_KEY")

set_api_key(eleven_labs_api_key)

def gettext():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    comp = openai.Completion.create(
          model="gpt-3.5-turbo-instruct",
          temperature=1.9,
          top_p=0.4,
          stream=False,
          max_tokens=1050,
          stop=["\n\n\n\n", "\n10. "],
          prompt=f"SYSTEM: output a list of interesting  and random facts about either NYC, technology, Brooklyn, History, science, inspirational quotes and passages from historic figures and books, etc. It must be in a list format, \nLIST OF IDEAS/FACTS :\n1. "
    )
    comp = comp.choices[0].text
    print(comp)
    for chunk in openai.Completion.create(
      model="gpt-3.5-turbo-instruct",
      stream=True,
      max_tokens=2550,
      stop=["\n\n\n\n"],
      temperature=1.9,
      top_p=0.4,
      prompt=f"SYSTEM: Greet Anton home and provide some interesting information to Anton from the list:\n{comp}\nMention the date and time of day\nGreeting for Anton at {date}:"
      ):
         print(chunk['choices'][0]['text'])
         yield chunk['choices'][0]['text']

audio_stream = generate(
    text=gettext(),
    voice="hjUljYvGJsI6RPf2Vzc6",
    model="eleven_monolingual_v1",
    stream=True,
    latency=3,
    stream_chunk_size=2024,
)

stream(audio_stream) 
