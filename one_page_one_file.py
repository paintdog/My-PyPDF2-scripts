from PyPDF2 import PdfFileWriter, PdfFileReader
import os

files = [file for file in os.listdir() if file.endswith(".pdf")]

number = 1000

for file in files:
    # get the source
    input1 = PdfFileReader(open(file, "rb"))

    # one file to x files (one page == one file)
    for page in range(input1.getNumPages()):
        
        output = PdfFileWriter()
        output.addPage(input1.getPage(page))

        outputStream = open("{:04d}.pdf".format(number), "wb")
        output.write(outputStream)
        outputStream.close()

        number += 1
