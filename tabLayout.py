'''Copyright 2019 VogelLover'''
''' File to create outline of tabbed layout for Scoreboarder'''
#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import *
from FrameElements import *
import getConfig as config
from PIL import Image, ImageTk
import itertools
from functools import partial
from shutil import copy2

configuration = config.configuration
playerScore = []
charImgButton = []

class MakeTabLayout():
    def __init__(self, DefaultColour):
        self. defaultcolour = DefaultColour
        self.getCharImages()
        self.widget = Notebook()

        self.PlayerTab = makeFrameTab(self.widget)
        self.StageTab  = makeFrameTab(self.widget)
        self.ScoreTab  = makeFrameTab(self.widget)
        self.AboutTab  = makeFrameTab(self.widget)

        self.makePlayerTab()
        self.makeStageTab()
        self.makeScoreTab()
        self.makeAboutTab()

        self.widget.add(self.PlayerTab, text="Players") 
        self.widget.add(self.StageTab,  text="Stages")
        self.widget.add(self.ScoreTab,  text="Scores")
        self.widget.add(self.AboutTab,  text="About")
    
        self.widget.grid(row=1, column=1)


    #copy file to destination with a choice number in the name
    def copytodestinationwithname(self, path, filenamepart, count, photo):
        # for example will copy the file at path to "stage2.png" where filenamepart = "stage", 
        # choice is the radiobutton variable for stage and its value is currently 2
        # Same behaviour with player
        if filenamepart == 'player':
            choice = self.choiceOfPlayer.get()
            self.chosenChar[choice-1] = charImgButton[count]
            self.setIconToTab(choice, photo)
        else:
            self.chosenstage[choice.get()-1] = self.stagebutton[count]
            self.highlightChosenStage()
        copy2(path, config.destinationDirectory + filenamepart + str(choice) + ".png")

    # When a pop up window is closed, we reenable the button that calls it
    def popupWindowCloseAction(self, window, button):
        window.destroy()
        button.config(state=ACTIVE)

    def setIconToTab(self, playernumber, photo):
        self.imageLabel[playernumber - 1].config(image=photo)

    ''' Single function functions '''
    def makePlayerTab(self):
        '''Make radiobuttons to choose the player number to configure (allows setting name, score, character)'''
        self.imageLabel = []
        self.chosenChar = []
        self.choiceOfPlayer = IntVar()
        self.choiceOfPlayer.set(1)
        self.playerRadiobutton = makeRadiobuttonGroup(playerNumberArray, self.PlayerTab, self.choiceOfPlayer,0)

        for radio in self.playerRadiobutton:
            self.chosenChar.append(Button())
            playerScore.append(0)

        self.charChoiceButton = Button(self.PlayerTab, command=self.ShowCharactersWindow, text="Choose Character")
        self.charChoiceButton.grid(row=0, column=1, columnspan=2)
        rowval = 2
        colval = 0
        for player in self.playerRadiobutton:
            l = Label(self.PlayerTab, text="")
            l.grid(row=rowval, column=colval, columnspan=2)
            colval = colval + 2
            self.imageLabel.append(l)

    def getCharImages(self):
        self.charimg = []
        for img in config.charImages:
            self.charimg.append(ImageTk.PhotoImage(img))

    def ShowCharactersWindow(self):            
        self.filewin = Toplevel()
        '''Make a grid of buttons to set character icon for selected player (selected using player radio button)'''
        rowval = 1
        colval = 0
        buttoncount = 0
        rowval = rowval + 1

        for photo, path in itertools.zip_longest(self.charimg, config.charImagePaths):
            b = Button(self.filewin, image=photo, command=partial(self.copytodestinationwithname, path, "player", buttoncount, photo), activebackground='grey')
            buttoncount = buttoncount + 1
            charImgButton.append(b)
            b.grid(row=rowval, column=colval)
            colval = colval + 1
            if colval == 16 :
                colval = 0
                rowval = rowval + 1
        self.charChoiceButton.config(state=DISABLED)
        self.filewin.wm_protocol("WM_DELETE_WINDOW", func = partial(self.popupWindowCloseAction, self.filewin, self.charChoiceButton))
    def makeStageTab(self):
        label = Label(self.StageTab, text="Some frame elements here")
        label.grid(row=0, column=0)

    def makeScoreTab(self):
        label = Label(self.ScoreTab, text="otherthings")
        label.grid(row=0, column=0)

    def makeAboutTab(self):
        label = Label(self.AboutTab, text="Copyright-2019 VogelLover\r\nMade with love for use with SSBM\r\n"
            "To reach out to me or to read more on how to use Scoreboarder or to look at the source, go to:\n "
                "https://github.com/shrutidevasenapathy/Scoreboarder")
        label.grid(row=0, column=0)

