from PyPDF2 import PdfFileWriter, PdfFileReader


# Quelle einlesen und Ausgabe vorbereiten
output = PdfFileWriter()
input1 = PdfFileReader(open("document1.pdf", "rb"))


# Jede zweite Seite der Vorlage drehen
# Jede Seite der Vorlage der Ausgabe beigeben
for i, page in enumerate(range(input1.getNumPages())):
    if i in [8, 9]: # Hier werden die Seiten ausgewaehlt! Denke dran: 0, 1, 2 usw.
        output.addPage(input1.getPage(page))
    

# Neues Dokument ausgeben
outputStream = open("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()
