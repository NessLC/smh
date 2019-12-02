from io import StringIO
import os
import sys, getopt

  
def Multiple(lokDir, ulokDir):
    if lokDir == "": lokDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for lpdf in os.listdir(lokDir): #iterate through pdfs in pdf directory
        fileExtension = lpdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = lokDir + lpdf
            pdfFilenameOut = ulokDir + lpdf
            os.system('qpdf --password= --decrypt %s %s'%(pdfFilename, pdfFilenameOut))
     
lokDir = "/home/ness/Documents/projects/TesisMate/PDF/"
ulokDir = "/home/ness/Documents/projects/TesisMate/Updf/"
Multiple(lokDir, ulokDir)