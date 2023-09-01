import PyPDF2
from gtts import gTTS
import pygame
from io import BytesIO

# Function to convert PDF to text
def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to convert text to speech
def text_to_speech(text):
    speech = gTTS(text)
    return speech

# Function to play the generated speech
def play_speech(speech):
    pygame.mixer.init()
    speech_stream = BytesIO()
    speech.write_to_fp(speech_stream)
    speech_stream.seek(0)
    pygame.mixer.music.load(speech_stream)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# Main function
def main():
    pdf_path = "Small.pdf"  # Replace with the path to your PDF file
    extracted_text = pdf_to_text(pdf_path)
    generated_speech = text_to_speech(extracted_text)
    play_speech(generated_speech)

if __name__ == "__main__":
    main()
