from main import *
import numpy as nmp


class Item:
    def __init__(self, textBeforeItem, textAfterItem,itemTitle):
        self.textBeforeItem = textBeforeItem #sentenceBeforeItem
        self.textAfterItem = textAfterItem #sentenceAfterItem
        self.itemTitle = itemTitle 

ItemsToBeEtractedFromImgs=[] 
dataRows=[[]] 



def start():
    numberOfItemsToBeExtractedFromImg = int(input("Enter the Request Number: ")) # Number of items we want to get from the  file  
    pdfFilePath=input("Enter the path of the pdf file: ")
    for i in range(numberOfItemsToBeExtractedFromImg):
        textBeforeItem=input("Enter First Name: ")
        textAfterItem=input("Enter Second Name: ")
        itemTitle =input("Enter Title: ")
        ItemsToBeEtractedFromImgs.append(Item(textBeforeItem,textAfterItem,itemTitle))
    
    setFilesPath(pdfFilePath)
    
    clearNeededFiles()
    createNeededFiles() 
    convertPdfToImages(pdfFilePath, imagesFolderPath, poppler_path)
    addStudentNamesToStudentsList2()
    
    deleteFolder(imagesFolderPath)


def addStudentNamesToStudentsList2():
    images =getPathOfImagesINFolder(imagesFolderPath)
    dataExtractedRows = nmp.zeros( (len(images) ,len(ItemsToBeEtractedFromImgs) ),dtype=object )
    for i in range(len(images)) : # Loop on images
        allTextInImage = getTextInImage(images[i])
        for j in range(len(ItemsToBeEtractedFromImgs)): # Loop on each item that should be extracted from the image
            dataExtractedRows[i][j]= extractStudentNameFromText(ItemsToBeEtractedFromImgs[j].textBeforeItem, ItemsToBeEtractedFromImgs[j].textAfterItem, allTextInImage)

    WriteToExcel(dataExtractedRows,ItemsToBeEtractedFromImgs)
    #print(dataRows)


def WriteToExcel(dataRows,data):
    #Clear the excel file i[f exists]
    deleteFile(excelFileName)

    #Create/Open a workbook
    workbook = xlsxwriter.Workbook(excelFileName)

    #Create worksheet
    worksheet = workbook.add_worksheet()

    for i in range(len(data)):
        worksheet.write(0, i, data[i].itemTitle)


    
    for i in range(len(dataRows)):
        for j in range(len(dataRows[i])):
            worksheet.write(i+1, j, dataRows[i][j])
           # print(dataRows[i][i2] +" :" +str(i) +" :" +str(i2))
    workbook.close()

start()
