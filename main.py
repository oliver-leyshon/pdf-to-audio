import pyttsx3, PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdf_reader = PyPDF2.PdfReader(book)
pages = len(pdf_reader.pages)
print(pages)

for num in range(0, pages):
    page = pdf_reader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
    