import pytesseract as pt 
import cv2 

# pt.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseact.exe'

def ocr_text(img):
    txt = pt.image_to_string(img)
    return txt

# gray_image
def get_grayscale_image(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# noise reduction
def reducing_noise(img):
    return cv2.medianBlur(img, 5)

# Thresholding
def thresholding(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = cv2.imread('24.jpg')

img = get_grayscale_image(img)
img = reducing_noise(img)
img = thresholding(img)

text = ocr_text(img)

print(text) 