# utils.py
from PyPDF2 import PdfReader

def extract_text(file):
    if file.type == "application/pdf":
        reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    else:
        return file.read().decode("utf-8")
    


