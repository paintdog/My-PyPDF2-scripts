from PyPDF2 import PdfFileWriter, PdfFileReader
import os

files = [file for file in os.listdir() if file.endswith(".pdf")]

output = PdfFileWriter()
         
for file in files:
         
    input1 = PdfFileReader(open(file, "rb"))

    for page in range(input1.getNumPages()):
        output.addPage(input1.getPage(page))

outputStream = open("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()
