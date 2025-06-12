from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

def extract_text(file):
    if file.filename.endswith(".pdf"):
        images = convert_from_bytes(file.file.read())
        text = "\n".join(pytesseract.image_to_string(img) for img in images)
    elif file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img = Image.open(file.file)
        text = pytesseract.image_to_string(img)
    else:
        text = file.file.read().decode("utf-8")
    return text
