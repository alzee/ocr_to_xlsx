#!/usr/bin/python3

from PIL import Image

import pytesseract

imgname = '001.jpg'
img = Image.open(imgname)

Img = img.convert('L')


# print(pytesseract.image_to_string(Image.open(img)))
# print(pytesseract.image_to_string(Img))

# photo = Img.point(table, '1')
# photo.save("test.jpg")
print(pytesseract.image_to_string(Image.open('001.jpg'), lang='chi_sim'))

# print('fuck')

# print(pytesseract.image_to_string(img))

# print(pytesseract.image_to_string(Image.open(img), lang='fra'))

