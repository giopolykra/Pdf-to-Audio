# Pdf-to-Audio
Converts a pdf to an audio file

Run by tying:
python pdf-to-audio.py

You will be prompted to add the path of the pdf file you want to convert. The code will output an mp3 file called "audio.mp3" in the same folder as the pytohn file

# To do
- [ ] Because some pdf files have weird spacing, the PyPDF2 splits some of the words. I am thinking of converting the pdf into an image and then back to text and see if the issue dissapears
- [ ] The speach has some weird poses when you have line change. I have to see if removing the line change removes the issue.
