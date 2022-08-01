import cv2
import pytesseract
import glob, os
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

def getAllImagesINFolder(folder):
    images = []
    for dirpath,_,filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(".jpg"):
                images.append(os.path.abspath(os.path.join(dirpath, filename)))
    return images

def procces(path):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
    img = cv2.imread(path)
    #cv2.imshow("Image", img)
    return pytesseract.image_to_string(img)

# def excelWrite(dic, data,index: int):
#     for i in range(len(dic)):
        


# parametersCount = int(input("parameters Count"))

# dic=[];
# for x in range(parametersCount):
#     first = input("first Text");
#     second = input("2nd Text");
#     patameter = input("parameter name");
#     dic.append({"first":first, "2nd":second,"patameter":patameter})

for images in getAllImagesINFolder("./images"):
    print(images)
    print(procces(images))
    print("==============================================================================")



# def extract( start ,  end, data):
#    return (data.split(start))[1].split(end)[0]


cv2.waitKey(0)
cv2.destroyAllWindows()