from main import *


class Item:
    def __init__(self, firstName, secondName,title):
        self.firstName = firstName
        self.secondName = secondName
        self.title = title

data=[]
dataRows=[[]]
def start():
    eeqNumber= int(input("Enter the Request Number: "))
    pdfFilePath=input("Enter the path of the pdf file: ")
    for i in range(eeqNumber):
        firstName=input("Enter First Name: ")
        secondName=input("Enter Second Name: ")
        title =input("Enter Title: ")
        data.append(Item(firstName,secondName,title))
    
    setFilesPath(pdfFilePath)
    
    clearNeededFiles()
    createNeededFiles() 
    convertPdfToImages(pdfFilePath, imagesFolderPath, poppler_path)
    addStudentNamesToStudentsList2()
    
    deleteFolder(imagesFolderPath)


def addStudentNamesToStudentsList2():
    
    images =getPathOfImagesINFolder(imagesFolderPath)
    for i in range(len(images)) :
        text = getTextInImage(images[i])
        for i2 in range(len(data)):
            dataRows[i,i2]= extractStudentNameFromText(data[i2].firstName, data[i2].secondName, text)
    print(dataRows)
start()
