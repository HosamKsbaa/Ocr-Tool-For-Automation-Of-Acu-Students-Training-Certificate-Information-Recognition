from re import A
import cv2
import pytesseract
import glob, os
import xlsxwriter
from pdf2image import convert_from_path


# def addStudentNamesToStudentsList():
#     clearFile()
#     f = open("demofile2.txt", "a")
#     images =getPathOfImagesINFolder("./images")
#     for image in images :
#         text = getTextInImage(image)
#         studentName = extractStudentNameFromText("This is to certify that ", "has", text)
#         f.write("Name = "+ studentName +"\n")

#     f.close()




def getTextInImage(imagePath):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
    img = cv2.imread(imagePath)
    #cv2.imshow("Image", img)
    return pytesseract.image_to_string(img)
#

def getPathOfImagesINFolder(folderPath):
    images = []
    for dirpath,_,filenames in os.walk(folderPath):
        for filename in filenames:
            if filename.endswith(".jpeg"):
                images.append(os.path.abspath(os.path.join(dirpath, filename)))
    return images

def extractStudentNameFromText(textBeforeName, TextAfterName, allText):
    return (allText.split(textBeforeName))[1].split(TextAfterName)[0]

def writeStudentNamesIntoExcelSheet(names):

    clearFile("students.xlsx")
    #Create/Open a workbook
    workbook = xlsxwriter.Workbook('students.xlsx')

    #Create worksheet
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, "Name ")

    row = 1
    column = 0
    
    for name in names:
        worksheet.write(row, column, name)
        row += 1

    workbook.close()


def clearFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)


def addStudentNamesToStudentsList():
    images =getPathOfImagesINFolder("./images")
    for image in images :
        text = getTextInImage(image)
        studentName = extractStudentNameFromText("This is to certify that ", "has", text)
        studentsNames.append(studentName)




def convertPdfToImages(pdf_path, saving_folder, poppler_path):
    pages = convert_from_path(pdf_path=pdf_path,poppler_path=poppler_path)
    c=1
    for page in pages:
        img_name=f"img-{c}.jpeg"
        page.save(os.path.join(saving_folder,img_name),"JPEG")
        c+=1

studentsNames = []

poppler_path=r"M:\Popler\poppler-22.04.0\Library\bin"

pdf_path=r"./pdfFiles/DOC.pdf"
saving_folder = r"./images"


convertPdfToImages(pdf_path, saving_folder, poppler_path)

addStudentNamesToStudentsList()

writeStudentNamesIntoExcelSheet(studentsNames)



