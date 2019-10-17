import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# im = Image.open("test.png") # the second one
# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.save('temp2.jpg')
pytesseract.pytesseract.tesseract_cmd ='D:/Program Files/Tesseract-OCR/tesseract.exe' 
text = pytesseract.image_to_string(Image.open('test.png'))
print(text)
