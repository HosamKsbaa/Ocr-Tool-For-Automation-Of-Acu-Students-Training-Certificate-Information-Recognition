import cv2
import pytesseract
import glob, os



def getPathOfImagesINFolder(folderPath):
    images = []
    for dirpath,_,filenames in os.walk(folderPath):
        for filename in filenames:
            if filename.endswith(".jpg"):
                images.append(os.path.abspath(os.path.join(dirpath, filename)))
    return images

def getTextInImage(imagePath):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
    img = cv2.imread(imagePath)
    #cv2.imshow("Image", img)
    return pytesseract.image_to_string(img)


def writeTextInFile():
    f = open("demofile2.txt", "a")
    for images in getPathOfImagesINFolder("./images"):
        f.write(getTextInImage(images))
    f.close()

    
writeTextInFile()

cv2.waitKey(0)
cv2.destroyAllWindows()



