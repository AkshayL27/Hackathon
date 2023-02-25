import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = os.environ.get('TESSERACT_PATH', 'tesseract')

def recognize_text(image):
    text = pytesseract.image_to_string(Image.open(image))
    return text
