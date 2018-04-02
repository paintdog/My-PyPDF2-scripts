from PyPDF2 import PdfFileWriter, PdfFileReader

# get the source
input1 = PdfFileReader(open("__original__.pdf", "rb"))


number = 1000


# one file to x files (one page == one file)
for page in range(input1.getNumPages()):
    
    output = PdfFileWriter()
    output.addPage(input1.getPage(page))

    outputStream = open("{:04d}.pdf".format(number), "wb")
    output.write(outputStream)
    outputStream.close()

    number += 1
