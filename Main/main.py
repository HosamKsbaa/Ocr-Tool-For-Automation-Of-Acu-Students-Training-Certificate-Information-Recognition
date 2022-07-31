import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\work\AppData\Local\Tesseract-OCR\tesseract.exe'

img = cv2.imread("image.jpg")

cv2.imshow("Image", img)
text = pytesseract.image_to_string(img)
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()