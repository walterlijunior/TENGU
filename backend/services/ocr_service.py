from pytesseract import image_to_string
from PIL import Image

def extract_text_from_image(image_path)
    image = Image.open(image_path)
    text = image_to_string(image)
    return text