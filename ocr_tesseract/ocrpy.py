import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


pytesseract.pytesseract.tesseract_cmd ='D:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open('test.png'))
print(text)
