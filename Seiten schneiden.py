'''
from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger

pdf_file = PdfFileReader(open("Textanhang.pdf","rb"))
page = pdf_file.getPage(0)
print(page.cropBox.getLowerLeft())
print(page.cropBox.getLowerRight())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())
'''

from PyPDF2 import PdfFileWriter, PdfFileReader

with open("Document.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print("document has %s pages." % numPages)

    for i in range(numPages):
        page = input1.getPage(i)
        print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        # page.trimBox.lowerLeft = (0, 0)
        # page.trimBox.upperRight = (535, 0)
        page.cropBox.lowerLeft = (0, 160)
        page.cropBox.upperRight = (535, 1530)
        output.addPage(page)

    with open("out.pdf", "wb") as out_f:
        output.write(out_f)
