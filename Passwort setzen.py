import datetime
import os
import winsound

from PyPDF2 import PdfFileWriter, PdfFileReader

password = "PASSWORD"   # Change this to 1234 in production!!!


winsound.Beep(2000,200)
winsound.Beep(2000,200)


files = [file for file in os.listdir() if not file.startswith("__protected ") and file.endswith(".pdf") or file.endswith(".PDF")]


for file in files:

    t1 = datetime.datetime.now()

    # Quelle einlesen und Ausgabe vorbereiten
    output = PdfFileWriter()
    input_pdf = PdfFileReader(open(file, "rb"))

    output.appendPagesFromReader(input_pdf)
    output.encrypt(password)

    # Neues Dokument ausgeben
    outputStream = open("__protected {}".format(file), "wb")
    output.write(outputStream)
    outputStream.close()

    winsound.Beep(2000,200)
    winsound.Beep(2000,200)

    t2 = datetime.datetime.now()

    print("I needed  {}  seconds.".format((t2 - t1).total_seconds()))
