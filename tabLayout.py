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
from Coreboarder import *

configuration = config.configuration

class MakeTabLayout():
    def defineSelfVariables(self):
        self.PlayerTab = makeFrameTab(self.widget)
        self.StageTab  = makeFrameTab(self.widget)
        self.AboutTab  = makeFrameTab(self.widget)
        self.charImageCopy       = []
        self.stageImageCopy      = []
        self.playerIconLabel     = []
        self.chosenChar          = []
        self.playerScore         = []
        self.choiceOfPlayer      = IntVar()
        self.charImageButton     = []
        self.stageImageButton    = []
        self.chosenstage         = []
        self.stagebutton         = []
        self.stageImageLabel     = []
        self.choiceOfStage       = IntVar()
        self.choiceOfMatchNumber = IntVar()
        self.playerNameTextbox   = Entry()
        self.getImages()

    def __init__(self, DefaultColour):
        self.widget = Notebook()
        self.defaultcolour = DefaultColour
        self.defineSelfVariables()

        self.makePlayerMenu(self.PlayerTab)
        self.makeStageMenu (self.StageTab )
        self.makeAboutTab  (self.AboutTab)
        self.widget.add(self.PlayerTab, text="Players") 
        self.widget.add(self.StageTab,  text="Stages")
        self.widget.add(self.AboutTab,  text="About")
        self.widget.grid(row=1, column=1)

    #copy file to destination with a choice number in the name
    def copytodestinationwithname(self, path, filenamepart, count, photo):
        # for example will copy the file at path to "stage2.png" where filenamepart = "stage", 
        # choice is the radiobutton variable for stage and its value is currently 2
        # Same behaviour with player
        if filenamepart == 'player':
            choice = self.choiceOfPlayer.get()
            self.chosenChar[choice - 1] = self.charImageButton[count]
            setIconToLabel(self.playerIconLabel, choice - 1, photo)
        else:
            choice = self.choiceOfStage.get()
            self.chosenstage[choice - 1] = self.stagebutton[count]
            setIconToLabel(self.stageImageLabel, choice - 1, photo)
        copy2(path, config.destinationDirectory + filenamepart + str(choice) + ".png")

    # Get all images (for stage images and char images) and save a local copy
    def getImages(self):
        for img in config.charImages:
            self.charImageCopy.append(ImageTk.PhotoImage(img))
        for img in config.stageImages:
            img = img.resize((50,50))
            self.stageImageCopy.append(ImageTk.PhotoImage(img))

    # Create a pop up window with image buttons of stages
    def ShowStagesWindow(self):  
        self.stageWindow = Toplevel()          
        self.stageWindow.resizable(width=False, height=False)
        self.stagebutton.extend(makeImageButtonGrid(self.stageWindow, self.stageImageCopy, config.stageImagePaths, self.copytodestinationwithname,"stage"))
        self.stageChoiceWinButton.config(state=DISABLED)
        self.stageWindow.wm_protocol("WM_DELETE_WINDOW", func = partial(popupWindowCloseAction, self.stageWindow, self.stageChoiceWinButton))
        '''end of function'''

    # Create a pop up window with image buttons of chars
    def ShowCharactersWindow(self):            
        self.charWindow = Toplevel()
        self.charWindow.resizable(width=False, height=False)
        self.charImageButton.extend(makeImageButtonGrid(self.charWindow, self.charImageCopy, config.charImagePaths, self.copytodestinationwithname,"player"))
        self.charChoiceButton.config(state=DISABLED)
        self.charWindow.wm_protocol("WM_DELETE_WINDOW", func = partial(popupWindowCloseAction, self.charWindow, self.charChoiceButton))

    #Set the number of matches for the Stages display
    def setMatches(self):
        matchesCount = self.choiceOfMatchNumber.get()
        if matchesCount == 3:
            self.choiceOfStage.set(1)
            self.stageRadiobutton[3]['state'] ="disabled"
            self.stageRadiobutton[4]['state'] ="disabled"
            copy2(config.stagesDirectory+"default.png", config.destinationDirectory + "stage4.png")
            copy2(config.stagesDirectory+"default.png", config.destinationDirectory + "stage5.png")
            setIconToLabel(self.stageImageLabel, 3, self.stageImageCopy[1])
            setIconToLabel(self.stageImageLabel, 4, self.stageImageCopy[1])
        else:
            self.stageRadiobutton[3]['state'] ="normal"
            self.stageRadiobutton[4]['state'] ="normal"

    def makePlayerMenu(self, framename):
        ''' Makes a button to get icon choice pop up window = CharChoiceButtonFrame
            Makes radiobuttons to select player = PlayerRadioButtonFrame
            Makes an (empty) row to hold selected characters for each player = PlayerRadioButtonFrame
            Makes a textbox and button to set player names = EnterPlayerNameFrame'''

        CharChoiceButtonFrame  = Frame(framename)
        PlayerRadioButtonFrame = Frame(framename)
        EnterPlayerNameFrame   = Frame(framename)

        CharChoiceButtonFrame.grid(row=0, column=0)
        PlayerRadioButtonFrame.grid(row=1, column=0)
        EnterPlayerNameFrame.grid(row=2, column=0)
        
        #CharChoiceButtonFrame
        self.charChoiceButton = Button(CharChoiceButtonFrame, command=self.ShowCharactersWindow, text="Choose Character")
        self.charChoiceButton.grid(row=0, column=0)

        #PlayerRadioButtonFrame
        self.choiceOfPlayer.set(1)
        self.playerRadiobutton = makeRadiobuttonGroup(playerNumberArray, PlayerRadioButtonFrame, self.choiceOfPlayer, partial(self.clearTextbox, self.playerNameTextbox))
        for radio in self.playerRadiobutton:
            radio.grid_configure(sticky=E)
            self.chosenChar.append(Button())
            self.playerScore.append(0)
        colval = 0
        for player in self.playerRadiobutton:
            l = Label(PlayerRadioButtonFrame, text="")
            l.grid(row=1, column=colval)
            colval = colval + 1
            self.playerIconLabel.append(l)

        #EnterPlayerNameFrame
        self.playerName = StringVar()
        Label(EnterPlayerNameFrame, text="Player name").grid(row=0,column=0)
        self.playerNameTextbox = Entry(EnterPlayerNameFrame, textvariable=self.playerName)
        self.playerNameTextbox.grid(row=0, column=1)
        self.playerNameTextbox.bind('<Return>', self.setPlayerName)
        Button(EnterPlayerNameFrame, text="Set name", command=self.setPlayerName).grid(row=0, column=3)

    def clearTextbox(self, event=None):
        self.playerNameTextbox.delete(0, 'end')

    def setPlayerName(self, event=None):
        name   = self.playerName.get()
        player = self.choiceOfPlayer.get()
        if name == "":
            name = "Player " + str(player)
        self.playerRadiobutton[player-1].config(text=name)
        filename = config.playerNameDirectory + "Player"+str(player)+'.txt'
        writeStringToFileName(filename, name)

    def makeStageMenu(self, framename):
        '''Make button to get pop up window for stage choice
        Make radiobuttons for choice between Three Matcher and Five Matcher
        Make radiobuttons to choose Stage to set stage image for
        Make (empty) labels that contain Stage images (when they are set)'''
        #1
        self.stageChoiceWinButton = Button(framename, command=self.ShowStagesWindow, text="Choose Stage")
        self.stageChoiceWinButton.grid(row=0, column=0)
        #2
        self.choiceOfMatchNumber.set(5)
        self.matchCount = makeRadiobuttonGroup(matchCountArray, framename, self.choiceOfMatchNumber, self.setMatches)
        #3
        self.choiceOfStage.set(1)
        self.stageRadiobutton = makeRadiobuttonGroup(matchNumberArray, framename, self.choiceOfStage, 0)
        for radio in self.stageRadiobutton:
            self.chosenstage.append(Button())
        #4
        rowval = 2
        colval = 0
        for match in self.stageRadiobutton:
            l = Label(framename, text="")
            l.grid(row=rowval, column=colval)
            colval = colval + 1
            self.stageImageLabel.append(l)


    def makeAboutTab(self, framename):
        label = Label(framename, text="Copyright-2019 VogelLover\r\nCustom-made with love for SSBM\r\n"
            "To report issues, make suggestions/requests, go to:\n "
                "https://github.com/shrutidevasenapathy/Scoreboarder")
        label.grid(row=0, column=0)

