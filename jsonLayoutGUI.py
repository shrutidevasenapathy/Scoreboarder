#!/usr/bin/python3

import json
from tkinter import *
from functools import partial
from os import walk
from PIL import Image, ImageTk
import itertools
from shutil import copy2

with open('C:\\Users\\sdevasenapathy\\Documents\\Scoreboarder\\guilayout.json') as layoutlist:
    layout = dict(json.load(layoutlist))


class App:
    def __init__(self, master):
        matchgridrow = 0
        stagechoicegridrow = 1
        stageimagegridrow = 2
        playergridrow = 3
        charsgridrow = 4

        self.matchframe = Frame(master)
        self.matchframe.grid(row=matchgridrow)

        self.stageimageframe = Frame(master)
        self.stageimageframe.grid(row=stageimagegridrow)

        self.stagechoiceframe = Frame(master)
        self.stagechoiceframe.grid(row=stagechoicegridrow)

        self.playerframe = Frame(master)
        self.playerframe.grid(row=playergridrow)

        self.charsframe = Frame(master)
        self.charsframe.grid(row=charsgridrow)

        #Make match numbers radiobuttons
        self.matchchoice = IntVar()
        self.matchchoice.set(5)
        self.matches3 = Radiobutton(self.matchframe, text="Three Matches", variable=self.matchchoice, value=3, command=self.setMatches)
        self.matches3.grid(row=matchgridrow,column=2)
        self.matches5 = Radiobutton(self.matchframe, text="Five Matches", variable=self.matchchoice, value=5, command=self.setMatches)
        self.matches5.grid(row=matchgridrow, column=4)
        
        # Make all stage radiobuttons
        self.stagechoice = IntVar()
        self.stagechoice.set(1)
        self.stagebutton = []
        for radiobutton in layout['stagenumber']:
            x = Radiobutton(self.stagechoiceframe, text=radiobutton["label"], variable=self.stagechoice, value=radiobutton["value"])#command=partial(self.setStage, radiobutton["value"]))
            self.stagebutton.append(x)
            x.grid(row= radiobutton['row'], column= radiobutton['column'])

        #Make all stage icons into a row of buttons
        self.photo = []
        rowval = stageimagegridrow
        colval = 0
        for img in stageImages:
            img = img.resize((50,50))
            self.photo.append(ImageTk.PhotoImage(img))
        for photo, path in itertools.zip_longest(self.photo, stageImagePaths):
            self.button = Button(self.stageimageframe, image=photo, command=partial(self.copytodestinationwithname, path, "stage", self.stagechoice, 0), activebackground='grey')
            self.button.grid(row=rowval, column=colval)
            colval = colval + 1
            if colval == 12 :
                colval = 0
                rowval = rowval + 1

        # Make all player radiobuttons
        self.playerchoice = IntVar()
        self.playerchoice.set(1)
        self.chosencharacter = []
        #self.chosencharacter.append(Button())
        for radiobutton in layout['playernumber']:
            self.rb = Radiobutton(self.playerframe, text=radiobutton["label"], variable=self.playerchoice, value=radiobutton["value"],command=self.highlightChosenChar)
            self.rb.grid(row= radiobutton['row'], column= radiobutton['column'])
            self.chosencharacter.append(Button())

        print(self.chosencharacter)
        #Make all characters icons into a grid of buttons
        self.charimg = []
        self.charbutton = []
        rowval = charsgridrow
        colval = 0
        buttoncount = 0
        for img in charImages:
            self.charimg.append(ImageTk.PhotoImage(img))
        for photo, path in itertools.zip_longest(self.charimg, charImagePaths):
            b = Button(self.charsframe, image=photo, command=partial(self.copytodestinationwithname, path, "player",self.playerchoice, buttoncount), activebackground='grey')
            buttoncount = buttoncount + 1
            self.charbutton.append(b)
            b.grid(row=rowval, column=colval)
            colval = colval + 1
            if colval == 12 :
                colval = 0
                rowval = rowval + 1 

    #copy file to destination with a choice number in the name
    def copytodestinationwithname(self, path, filenamepart, choice, count):
        # for example will copy the file at path to "stage2.png" where filenamepart = "stage", 
        # choice is the radiobutton variable for stage and its value is currently 2
        # Same behaviour with player
        if filenamepart == 'player':
            #for button in self.charbutton:
            self.chosencharacter[choice.get()-1] = self.charbutton[count]
            self.highlightChosenChar()
        else:
            self.stagebutton[count]['background'] = 'blue'
        self.chosencharacter[choice.get()-1] = self.charbutton[count]
        copy2(path, destinationDirectory + filenamepart + str(choice.get()) + ".png")
    #Highlight the chosen character with a coloured box around the character icon button
    def highlightChosenChar(self):
        player = self.playerchoice.get()
        for button in self.charbutton:
            button['background'] = DefaultColour
        self.chosencharacter[player-1]['background'] = 'blue'
        print(self.chosencharacter[player-1])

    #Set the number of matches for the Stages display
    def setMatches(self):
        self.matchesCount = self.matchchoice.get()
        if self.matchesCount == 3:
            self.stagebutton[3]['state'] ="disabled"
            self.stagebutton[4]['state'] ="disabled"
            copy2(stagesDirectory+"default.png", destinationDirectory + "stage4.png")
            copy2(stagesDirectory+"default.png", destinationDirectory + "stage5.png")
        else:
            self.stagebutton[3]['state'] ="normal"
            self.stagebutton[4]['state'] ="normal"

def getFilesListFrom(directorypath):
    fileslist = []
    for (dirpath, dirnames, filenames) in walk(directorypath):
        fileslist.extend(filenames)
        break
    return fileslist


def getAllImagesFrom(dir):
    files = getFilesListFrom(dir)
    images = []
    filepaths = []
    for imagefilename in files:
        images.append(Image.open(dir + imagefilename))
        filepaths.append(dir + imagefilename)
    return images, filepaths

stagesDirectory = layout['Stages']
destinationDirectory = layout['OBSFolder']

charImages, charImagePaths = getAllImagesFrom(layout['Icons'])
stageImages, stageImagePaths = getAllImagesFrom(layout['Stages'])



root = Tk()
DefaultColour = root.cget("bg")

app = App(root)
root.mainloop()
root.destroy()
