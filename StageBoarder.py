from tkinter import *
from shutil import copy2
import os
from functools import partial
from os import walk
from PIL import Image, ImageTk

charIconsDirectory = 'C:/Users/sdevasenapathy/Documents/Scoreboarder/char-icons/'
stagesDirectory = 'C:/Users/sdevasenapathy/Documents/Scoreboarder/stages/'
destinationDirectory = 'C:/Users/sdevasenapathy/Documents/OBSFolder/'
matchNumbers = ["1", "2", "3", "4", "5"]

class App:
    def makeDropDownMenu(self, labeltext, menuitems, framelement, r, c):
        label = StringVar(framelement)
        label.set(labeltext)
        self.dropdownLabel = StringVar(framelement)
        self.dropdownLabel = Label(framelement, textvariable=label).grid(row=r,column=c)
        self.dropdown = StringVar(framelement)
        self.dropdown.set(menuitems[0]) # default value

        self.optionMenu = OptionMenu(framelement, self.dropdown, *menuitems).grid(row=r, column=c+1)

        return self.dropdown
    def setMatches(self):
        if self.var.get():
            self.matchesCount = self.var.get()
        else:
            self.matchesCount = 5
        print (self.matchesCount)
        copy2(stagesDirectory+"blank.png", destinationDirectory + "stage2.png")
        copy2(stagesDirectory+"blank.png", destinationDirectory + "stage4.png")

    def __init__(self, master):
        rowval = 0
        self.frame = Frame(master)
        self.frame.grid(row=rowval)
        self.var = IntVar()
        self.imageInfo = Label(self.frame)
        Radiobutton(self.frame, text="3 Matches", variable=self.var, value=3, command=self.setMatches).grid(row=rowval, column=1)
        Radiobutton(self.frame, text="5 Matches", variable=self.var, value=5, command=self.setMatches).grid(row=rowval, column=3)
        rowval = rowval + 1

        self.stagemenu = self.makeDropDownMenu("Stage", stages, self.frame, rowval, 0)
        self.matchmenu = self.makeDropDownMenu("Match", matchNumbers, self.frame, rowval, 2)
        self.SetStage = Button(self.frame, text="Set Stage", command=self.setImageStage).grid(row=rowval, column=4)
        rowval = rowval + 1

        self.charmenu1= self.makeDropDownMenu("Player 1", characters, self.frame, rowval, 0)
        self.color1= self.makeDropDownMenu("Color", colors, self.frame, rowval, 2)
        self.SetChar1 = Button(self.frame, text="Set Icon", command=partial(self.setImagePlayerChar, 1, self.charmenu1, self.color1, self.imageInfo))
        self.SetChar1.grid(row=rowval,column=4)

        rowval = rowval + 1

        self.charmenu2= self.makeDropDownMenu("Player 2", characters, self.frame, rowval, 0)
        self.color2= self.makeDropDownMenu("Color", colors, self.frame, rowval, 2)
        self.SetChar2 = Button(self.frame, text="Set Icon", command=partial(self.setImagePlayerChar, 2, self.charmenu2, self.color2))
        self.SetChar2.grid(row=rowval,column=4)

        rowval = rowval + 1

        self.charmenu3 = self.makeDropDownMenu("Player 3", characters, self.frame, rowval, 0)
        self.color3= self.makeDropDownMenu("Color", colors, self.frame, rowval, 2)
        self.SetChar3 = Button(self.frame, text="Set Icon", command=partial(self.setImagePlayerChar, 3, self.charmenu3, self.color3))
        self.SetChar3.grid(row=rowval,column=4)

        rowval = rowval + 1

        self.charmenu4= self.makeDropDownMenu("Player 4", characters, self.frame, rowval, 0)
        self.color4= self.makeDropDownMenu("Color", colors, self.frame, rowval, 2)
        self.SetChar4 = Button(self.frame, text="Set Icon", command=partial(self.setImagePlayerChar, 4, self.charmenu4, self.color4))
        self.SetChar4.grid(row=rowval,column=4)

        rowval = rowval + 1
        #self.photo = ImageTk.PhotoImage(img)
        #self.imageInfo = Label(self.frame, image=self.photo).grid(row=rowval,column=2)

    def setImageStage(self):
        for item in stages:
            if self.stagemenu.get() == item:
                n = self.matchmenu.get()
                if (self.matchesCount == 3):
                    print (n)
                    if (n == '2'):
                        n = '3'
                        print (n)
                    elif (n == '3'):
                        n = '5'
                        print (n)
                copy2(stagesDirectory+item+".png", destinationDirectory + "stage" + n + ".png")
    
    def setImagePlayerChar(self, playernum, iconmenu, colormenu, imagedisplay):
        for item in characters:
            if iconmenu.get() == item:
                c = colormenu.get()
                copy2(charIconsDirectory+item+"-"+c+".png", destinationDirectory + "char" + str(playernum) + ".png")
                filename = item + '-'+c+'.png'
                print(filename)
                #self.photo = ImageTk.PhotoImage(img)
                #imagedisplay.config(image=img)


characters = []
colors = []
stages = []
def getFilesListFrom(directorypath):
    fileslist = []
    for (dirpath, dirnames, filenames) in walk(directorypath):
        fileslist.extend(filenames)
        break
    return fileslist

#Get all character icon file names from the directory
charicons = getFilesListFrom(charIconsDirectory)
imagearray = []
images = 0
#Get characters and colors from filename (<charname>-<color>.png)
for charicon in charicons:
    splitbydash = charicon.split('-')
    characters.append(splitbydash[0])
    colorsplit = splitbydash[1].split('.')[0]
    colors.append(colorsplit)



#Remove duplicates from list of characters
characters = list( dict.fromkeys(characters) )
#Remove duplicates from list of colors
colors = list(dict.fromkeys(colors))

#Get names of stages from files in directory
stagenames = getFilesListFrom(stagesDirectory)



for stagename in stagenames:
    itemname = stagename.split('.')
    stages.append(itemname[0])


root = Tk()

app = App(root)

root.mainloop()
root.destroy()