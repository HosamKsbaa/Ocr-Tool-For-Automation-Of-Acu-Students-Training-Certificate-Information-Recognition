from re import A
import cv2
import pytesseract
import glob, os

def getTextInImage(imagePath):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
    img = cv2.imread(imagePath)
    #cv2.imshow("Image", img)
    return pytesseract.image_to_string(img)


def getPathOfImagesINFolder(folderPath):
    images = []
    for dirpath,_,filenames in os.walk(folderPath):
        for filename in filenames:
            if filename.endswith(".jpg"):
                images.append(os.path.abspath(os.path.join(dirpath, filename)))
    return images

def extractStudentNameFromText(textBeforeName, TextAfterName, allText):
    return (allText.split(textBeforeName))[1].split(TextAfterName)[0]


def clearFile():
    if os.path.exists("demofile2.txt"):
        os.remove("demofile2.txt")


def writeTextInFile():
    clearFile()

    f = open("demofile2.txt", "a")
    images =getPathOfImagesINFolder("./images")
    for image in images :
        text = getTextInImage(image)
        studentName = extractStudentNameFromText("This is to certify that ", "has", text)
        f.write("Name = "+ studentName +"\n")

    f.close()



writeTextInFile()

cv2.waitKey(0)
cv2.destroyAllWindows()



