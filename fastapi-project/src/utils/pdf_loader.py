from PyPDF2 import PdfReader
from io import BytesIO


def extract_text_from_pdf(file_bytes):
    reader = PdfReader(BytesIO(file_bytes))
    text = ""

    for page in reader.pages:
        text += (page.extract_text() or "") + "\n"

    # simple chunking
    chunks = text.split("\n")

    return [c.strip() for c in chunks if len(c.strip()) > 30]