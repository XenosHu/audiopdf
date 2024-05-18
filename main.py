# import streamlit as st
# import PyPDF2
# import io
# import os
# from streamlit_TTS import auto_play, text_to_speech, text_to_audio
# from openai import OpenAI
# from gtts.lang import tts_langs

# langs = list(tts_langs().keys())

# # Function to play audio directly
# def play_audio(audio):
#     auto_play(audio)

# # Function to convert text to speech and play the audio
# def convert_and_play(text, language='en', voice='male'):
#     audio = text_to_audio(text, language=language)
#     play_audio(audio)

# # Main Streamlit app
# def main():
#     st.title("Text-to-Speech Converter")

#     selected_lang = st.selectbox("Choose a language", options=langs)
#     selected_voice = st.selectbox("Choose a voice", ['male', 'female'])
#     text_input = st.text_input("Enter text to convert to speech")

#     if st.button("Speak"):
#         if text_input:
#             convert_and_play(text_input, language=selected_lang, voice=selected_voice)
#         else:
#             st.error("Please enter some text.")

# if __name__ == "__main__":
#     main()


import streamlit as st
from streamlit_TTS import auto_play, text_to_speech, text_to_audio

from gtts.lang import tts_langs

langs=tts_langs().keys()

#get the audio first
audio=text_to_audio("Choose a language, type some text, and click 'Speak it out!'.",language='en')
#then play it
auto_play(audio)

lang=st.selectbox("Choose a language",options=langs)
text=st.text_input("Choose a text to speak out:")
speak=st.button("Speak it out!")

if lang and text and speak:
    #plays the audio directly
    text_to_speech(text=text, language=lang)
