import os
from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader
# pyinstaller --onefile mergepdf.py

__version__ = '1.0.1'
def incdec(updown, num):
    if updown == "up":
        return num + 2
    else:
        return num - 2

# splitfiles
pageNum = 1
direction = "up"
counter =0
for filename in os.listdir("."):
    if filename.endswith(".pdf") and filename.startswith("CCF"):
        print("Splitting %s" % filename)

        inputpdf = PdfFileReader(open(filename, "rb"))

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("page%2s.pdf" % pageNum, "wb") as outputStream:
                output.write(outputStream)
            pageNum = incdec(direction, pageNum)
            counter = counter + 1

        pageNum=counter * 2
        direction = "down"

## mergefiles
mergedObject = PdfFileMerger()
for filename in os.listdir("."):
    if filename.endswith(".pdf") and filename.startswith("page"):
        print("Merging %s" % filename)
        mergedObject.append(PdfFileReader(filename, 'rb'))
        os.remove(filename)
mergedObject.write("mergedpdf.pdf")