from PyPDF2 import PdfFileWriter, PdfFileReader


# Quelle einlesen und Ausgabe vorbereiten
input1 = PdfFileReader(open("document1.pdf", "rb"))
output = PdfFileWriter()


# Jede Seite der Vorlage drehen und der Ausgabe beigeben
for page in range(input1.getNumPages()):
    output.addPage(input1.getPage(page).rotateClockwise(90))


# Neues Dokument ausgeben
outputStream = open("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()
