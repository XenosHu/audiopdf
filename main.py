import streamlit as st
import pyttsx3
import PyPDF2

def convert_pdf_to_audio(pdf_file, voice_gender):
    # Open the PDF file in binary mode
    with open(pdf_file, 'rb') as book:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(book)

        # Initialize text to store extracted content
        text = ""

        # Iterate through all the pages
        for page_num in range(pdf_reader.numPages):
            # Extract text from the page
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set the voice based on the selected gender
    voices = engine.getProperty('voices')
    if voice_gender == 'Male':
        engine.setProperty('voice', voices[0].id)  # Assuming male voice is the first one
    else:
        engine.setProperty('voice', voices[1].id)  # Assuming female voice is the second one

    # Convert text to speech
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()

    return 'output.mp3'

def main():
    st.title("PDF to Audio Converter")

    # Upload PDF file
    pdf_file = st.file_uploader("Upload PDF file", type=['pdf'])

    # Select voice gender
    voice_gender = st.selectbox("Select voice gender", ['Male', 'Female'])

    # Convert PDF to audio on button click
    if st.button("Convert to Audio"):
        if pdf_file is not None:
            audio_file = convert_pdf_to_audio(pdf_file, voice_gender)
            st.audio(audio_file, format='audio/mp3', start_time=0)

            # Provide download link
            st.markdown(f"Download the audio file [here](./{audio_file})")

if __name__ == "__main__":
    main()