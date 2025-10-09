# functiosn.py
from pypdf import PdfWriter
import  img2pdf
import io


# pdf mergin function completed
def merge(pdfs):
    pdfwriter = PdfWriter()

    for pdf in pdfs:
        pdfwriter.append(pdf)
    buffer = io.BytesIO()

    pdfwriter.write(buffer)
    buffer.seek(0)
    return buffer

def create(pdfs):
    pdf = img2pdf.convert([file.stream for file in pdfs])
    buffer = io.BytesIO(pdf)
    buffer.seek(0)
    return buffer