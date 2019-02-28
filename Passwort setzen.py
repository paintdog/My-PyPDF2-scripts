import datetime
import os
import winsound

from PyPDF2 import PdfFileWriter, PdfFileReader

password = "PASSWORD"   # Change this to 1234 in production!!!

t1 = datetime.datetime.now()

winsound.Beep(2000,200)
winsound.Beep(2000,200)

file = [file for file in os.listdir() if (file.endswith(".pdf") or file.endswith(".PDF")) and file != 'document-output.pdf'][-1]

# Quelle einlesen und Ausgabe vorbereiten
output = PdfFileWriter()
input_pdf = PdfFileReader(open(file, "rb"))

output.appendPagesFromReader(input_pdf)
output.encrypt(password)

# Neues Dokument ausgeben
outputStream = open("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()

winsound.Beep(2000,200)
winsound.Beep(2000,200)

t2 = datetime.datetime.now()

print("I needed  {}  seconds.".format((t2 - t1).total_seconds()))
