from pypdf import PdfWriter
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
