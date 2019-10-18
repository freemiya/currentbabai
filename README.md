# currentbabai
Simple app to send notifications about electricity updates in Twitter. Bangalore electricity board shares updates in the form of images.
![images](https://github.com/freemiya/currentbabai/blob/master/ocr_tesseract/test.png). 

I wanted an app, which would mail me, when my area is mentioned in a electricity update.

**Would be happy if you can share and develop this repo.**

Structure : 

<ul>
  <li>data/</li>
  <li>nbs/</li>
  <li>src/</li>
</ul>

Using PyTesseract requires two things : 

1. Installing library through pip : `pip install pytesseract`
2. Downloading OCR module separately.

# PyTesseract OCR module (For Windows):

1. Download .exe from [here](https://github.com/UB-Mannheim/tesseract/wiki)
2. During installation, place it in "C:\Program Files\Tesseract-OCR"
3. For more details, go [here](https://github.com/tesseract-ocr/tesseract/wiki)
