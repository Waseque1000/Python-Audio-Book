import pyttsx3
import PyPDF3
book = open('ott.pdf', 'rb')
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()

for num in range(7,pages):

    page = pdfReader.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()