from main import *
import numpy as nmp


class Item:
    def __init__(self, firstName, secondName,title):
        self.firstName = firstName #sentenceBeforeItem
        self.secondName = secondName #sentenceAfterItem
        self.title = title 

data=[] #ItemsEtractedFromImage
dataRows=[[]] 



def start():
    numberOfItemsToBeExtractedFromImg = int(input("Enter the Request Number: ")) # Number of items we want to get from the  file  
    pdfFilePath=input("Enter the path of the pdf file: ")
    for i in range(numberOfItemsToBeExtractedFromImg):
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
    dataRows = nmp.zeros( (len(images) ,len(data) ),dtype=object )
    for i in range(len(images)) :
        text = getTextInImage(images[i])
        #print(text)
        #print("==================")
        for i2 in range(len(data)):
            dataRows[i][i2]= extractStudentNameFromText(data[i2].firstName, data[i2].secondName, text)
            print(str(i) +" : "+str(i2))

    WriteToExcel(dataRows,data)
    #print(dataRows)


def WriteToExcel(dataRows,data):
    #Clear the excel file i[f exists]
    deleteFile(excelFileName)

    #Create/Open a workbook
    workbook = xlsxwriter.Workbook(excelFileName)

    #Create worksheet
    worksheet = workbook.add_worksheet()

    for i3 in range(len(data)):
        worksheet.write(0, i3, data[i3].title)


    
    for i in range(len(dataRows)):
        for i2 in range(len(dataRows[i])):
            worksheet.write(i+1, i2, dataRows[i][i2])
           # print(dataRows[i][i2] +" :" +str(i) +" :" +str(i2))
    workbook.close()

start()
