from PyPDF2 import PdfFileWriter, PdfFileReader


# Quelle einlesen und Ausgabe vorbereiten
output = PdfFileWriter()
input1 = PdfFileReader(open("document1.pdf", "rb"))


# Jede zweite Seite der Vorlage drehen
# Jede Seite der Vorlage der Ausgabe beigeben
for i, page in enumerate(range(input1.getNumPages())):
    if i % 2 == 0: # gerade - 0 2 4
        output.addPage(input1.getPage(page))
    else:          # ungerade - 1 3 5  ...
        output.addPage(input1.getPage(page).rotateClockwise(180))
    

# Neues Dokument ausgeben
outputStream = open("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()
