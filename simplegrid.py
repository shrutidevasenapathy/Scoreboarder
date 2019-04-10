from tkinter import *
from os import walk
from PIL import Image, ImageTk
from functools import partial
import itertools
from shutil import copy2
from time import sleep

iconsdir = "C:/Users/sdevasenapathy/Documents/Scoreboarder/char-icons/"
destinationDirectory = "C:/Users/sdevasenapathy/Documents/OBSFolder/"
stagesDirectory = 'C:/Users/sdevasenapathy/Documents/Scoreboarder/stages/'

imagesList = []
imagepath = []
n = "1"
def getFilesListFrom(directorypath):
    fileslist = []
    for (dirpath, dirnames, filenames) in walk(directorypath):
        fileslist.extend(filenames)
        break
    return fileslist

charfiles = getFilesListFrom(iconsdir)

for image in charfiles:
    imagesList.append(Image.open(iconsdir+image))
    imagepath.append(iconsdir+image)

stageImage = Image.open(stagesDirectory + "Dreamland.png")

class App:
    def makeButton(self, buttonlabel, commandname, r, c):
        button = Button(self.frame, text=buttonlabel, command=commandname).grid(row=r, column=c)
        return button

    def makeImageButton(self, frame, buttonimage, commandname, r, c):
        imageButton = Button(frame, command=commandname, image = buttonimage, activebackground='grey').grid(row=r, column=c)
        return imageButton

    def __init__(self, master):
        self.frameStages = Frame(master)
        stagegridrow = 0
        self.frameStages.grid(row=stagegridrow)

        self.frameChars = Frame(master)
        chargridrow = 2
        self.frameChars.grid(row=chargridrow)
        self.photo = []
        for i in imagesList:
            self.photo.append(ImageTk.PhotoImage(i))

        col = 0
        rowval = chargridrow + 1
        self.matchnumber = IntVar()
        self.stagephoto = ImageTk.PhotoImage(stageImage)
        
        rowval = rowval + 1
        #self.stageButton = self.makeImageButton(self.frameStages, self.stagephoto, partial(self.printsomething, "text"), rowval, col)
        self.stageButton = Button(text="textlabel", command=partial(self.printsomething, "text", state=DISABLED))#.grid(row=rowval, column=col)
        self.stageButton.grid(row=rowval, column=col)
        #self.stageButton['state'] =NORMAL
        rowval = rowval + 1
        Radiobutton(self.frameStages, text="3 Matches", variable=self.matchnumber, value=3, command=partial(self.setMatches, self.stageButton)).grid(row=rowval, column=col)
        Radiobutton(self.frameStages, text="5 Matches", variable=self.matchnumber, value=5, command=partial(self.setMatches, self.stageButton)).grid(row=rowval, column=col+2)
        
        rowval = rowval + 1

        for photo, path in itertools.zip_longest(self.photo, imagepath):
            self.button = self.makeImageButton(self.frameChars, photo, partial(self.printfile, path), rowval, col)
            col = col + 1
            if col == 12 :
                col = 0
                rowval = rowval + 1

    #All interface command callbacks here: 
    def printsomething(self, text):
        print ("something " + text)
    #Set the number of matches for the Stages display
    def setMatches(self, button):
        self.matchesCount = self.matchnumber.get()
        print (self.matchesCount)
        if self.matchesCount == 3:
            self.stageButton['state'] ="disabled"
            copy2(stagesDirectory+"blank.png", destinationDirectory + "stage2.png")
            copy2(stagesDirectory+"blank.png", destinationDirectory + "stage4.png")
        else:
            self.stageButton['state'] ="normal"   
    def printfile(self, filename):
        copy2(filename, destinationDirectory + "player"+n+".png")


    def getStage(self):
        for stage in stages:
            if stageName.get() == stage:
                copy2(stage+".png", destinationDirectory+"stage.png")

root = Tk()
app = App(root)
root.mainloop()
root.destroy()