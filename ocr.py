import os
import pytesseract
import cv2

# Set the tessdata directory explicitly
os.environ["TESSDATA_PREFIX"] = "/Users/praneethchetty/Documents/myprojects/Sanskrit/tessdata"

def detect(filename):
    img = cv2.imread(filename)
    text = pytesseract.image_to_string(img, lang='san')
    return text
