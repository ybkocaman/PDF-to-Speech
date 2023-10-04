from PyPDF2 import PdfReader
from gtts import gTTS
import subprocess


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ''
    try:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    except Exception as e:
        print(f"Error reading PDF: {str(e)}")
    return text


# Function to convert text to speech
def text_to_speech(text, output_file):
    if text.strip():  # Check if there is non-empty text to speak
        tts = gTTS(text)
        tts.save(output_file)
        subprocess.run(['open', output_file])  # Open the generated audio file (macOS)
    else:
        print("No text found in the PDF file.")


if __name__ == "__main__":
    pdf_file_path = "sample.pdf"  # Replace with the path to your PDF file
    output_audio_file = "output.mp3"  # Output audio file name

    extracted_text = extract_text_from_pdf(pdf_file_path)
    text_to_speech(extracted_text, output_audio_file)
