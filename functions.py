from pypdf import PdfWriter

# pdf mergin function completed
def merge(pdfs, output):
    pdfwriter = PdfWriter()
    
    for pdf in pdfs:
        pdfwriter.append(pdf)
    
    with open(output,'wb') as f:
        pdfwriter.write(f)

