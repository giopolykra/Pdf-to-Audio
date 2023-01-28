import PyPDF2
from gtts import gTTS

def main():
    # Open the PDF file
    file_path = input("Please enter the file path:\n")
    corverter(file_path)

def corverter(file_path):
        with open(file_path, 'rb') as file:
            # Create a PDF reader object
            reader = PyPDF2.PdfFileReader(file)
            # Extract the text from the first page
            text = reader.getPage(0).extractText()
            # Create a gTTS object and save the audio file
            tts = gTTS(text)
            tts.save('audio.mp3')
            
if __name__ == "__main__":
    main()