mergepdf
========

version 1.0

The problem
-----------
At home, I scan my documents and store them as PDF format.  My printer has a document feeder which will scan
one side of the document.  Then I will need to take the stack of pages, and turn it around to scan the back
of the document.

So when I scan front side of the document, it creates one pdf and
when I scan the back of the document, it creates another pdf.

What I would like to do is to generate a pdf with all pages of the document with the pages in the correct order.

Solution
--------
Let's assume when I scan the front side of all pages of the document, the resulting name is:  CCF08292020_0000.pdf
Let's assume when I scan the back side of all pages of the document, the resulting name is:  CC08292020_0001.pdf

The naming convention, my scanning software use is CCF<mmddyyy>__<sequence number>.pdf


As an illustration to clarify the problem, my page numbers would end up as follows:

After scanning front pages of my document, I would get a pdf with the following:
pages scanned in the pdf are:  1, 3, 5, 7

After scanning back pages of my document, I would get a pdf with the following:
pages scanned are:  8, 6, 4, 2

So this script will take take each pdf and splits them up into individual pages and then merge them together
with all the pages in the correct order.

The script will assume the file name starts with CCF<sequence number>.  For example: CCF08292020_00000.pdf
The script will assume the lower sequence number is the front pages scanned and the higher sequence number file
contains the back pages scanned. 

