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
charImgButton = []

class MakeTabLayout():
    def __init__(self, DefaultColour):

        self. defaultcolour = DefaultColour
        self.getImages()

        self.widget = Notebook()

        self.PlayerTab = makeFrameTab(self.widget)
        self.StageTab  = makeFrameTab(self.widget)
        self.ScoreTab  = makeFrameTab(self.widget)
        self.AboutTab  = makeFrameTab(self.widget)

        self.makePlayerMenu(self.PlayerTab)
        self.makeStageMenu (self.StageTab )
        self.makeScoreTab  (self.ScoreTab)
        self.makeAboutTab  (self.AboutTab)

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
            self.chosenChar[choice - 1] = charImgButton[count]
            self.setIconToLabel(self.imageLabel, choice - 1, photo)
        else:
            choice = self.stagechoice.get()
            self.chosenstage[choice - 1] = self.stagebutton[count]
            self.setIconToLabel(self.stageImageLabel, choice - 1, photo)
        copy2(path, config.destinationDirectory + filenamepart + str(choice) + ".png")

    # When a pop up window is closed, we reenable the button that calls it
    def popupWindowCloseAction(self, window, button):
        window.destroy()
        button.config(state=ACTIVE)

    def setIconToLabel(self, labelarray, index, photo):
        labelarray[index].config(image=photo)
    
    def makeImageButtonGrid(self, framename, imgarray, patharray, action, typestring):
        rowval = 1
        colval = 0
        buttoncount = 0
        rowval = rowval + 1
        buttonarray = []
        for photo, path in itertools.zip_longest(imgarray, patharray):
            b = Button(framename, image=photo, command=partial(action, path, typestring, buttoncount, photo), activebackground='grey')
            buttoncount = buttoncount + 1
            buttonarray.append(b)
            b.grid(row=rowval, column=colval)
            colval = colval + 1
            if colval == 16 :
                colval = 0
                rowval = rowval + 1
        return buttonarray

    ''' Single function functions '''
    # Get all images (for stage images and char images) and save a local copy
    def getImages(self):
        self.charimg = []
        self.stageimage = []
        for img in config.charImages:
            self.charimg.append(ImageTk.PhotoImage(img))
        for img in config.stageImages:
            img = img.resize((50,50))
            self.stageimage.append(ImageTk.PhotoImage(img))

    # Create a pop up window with image buttons of stages
    def ShowStagesWindow(self):            
        self.stageWindow = Toplevel()
        self.stageWindow.resizable(width=False, height=False)
        self.stagebutton.extend(self.makeImageButtonGrid(self.stageWindow, self.stageimage, config.stageImagePaths, self.copytodestinationwithname,"stages"))
        self.stageChoiceWinButton.config(state=DISABLED)
        self.stageWindow.wm_protocol("WM_DELETE_WINDOW", func = partial(self.popupWindowCloseAction, self.stageWindow, self.stageChoiceWinButton))
        '''end of function'''

    # Create a pop up window with image buttons of chars
    def ShowCharactersWindow(self):            
        self.charWindow = Toplevel()
        self.charWindow.resizable(width=False, height=False)
        charImgButton.extend(self.makeImageButtonGrid(self.charWindow, self.charimg, config.charImagePaths, self.copytodestinationwithname,"player"))
        self.charChoiceButton.config(state=DISABLED)
        self.charWindow.wm_protocol("WM_DELETE_WINDOW", func = partial(self.popupWindowCloseAction, self.charWindow, self.charChoiceButton))

    #Set the number of matches for the Stages display
    def setMatches(self):
        self.matchesCount = self.matchchoice.get()
        if self.matchesCount == 3:
            self.stagechoice.set(1)
            self.stageRadiobutton[3]['state'] ="disabled"
            self.stageRadiobutton[4]['state'] ="disabled"
            copy2(config.stagesDirectory+"default.png", config.destinationDirectory + "stage4.png")
            copy2(config.stagesDirectory+"default.png", config.destinationDirectory + "stage5.png")
            self.setIconToLabel(self.stageImageLabel, 3, self.stageimage[1])
            self.setIconToLabel(self.stageImageLabel, 4, self.stageimage[1])
        else:
            self.stageRadiobutton[3]['state'] ="normal"
            self.stageRadiobutton[4]['state'] ="normal"

    def makePlayerMenu(self, framename):
        '''Make radiobuttons to choose the player number to configure (allows setting name, score, character)'''
        self.imageLabel = []
        self.chosenChar = []
        self.playerScore = []
        self.choiceOfPlayer = IntVar()
        self.choiceOfPlayer.set(1)

        self.playerRadiobutton = makeRadiobuttonGroup(playerNumberArray, framename, self.choiceOfPlayer,0)
        for radio in self.playerRadiobutton:
            self.chosenChar.append(Button())
            self.playerScore.append(0)

        self.charChoiceButton = Button(framename, command=self.ShowCharactersWindow, text="Choose Character")
        self.charChoiceButton.grid(row=0, column=1, columnspan=2)

        rowval = 2
        colval = 0
        for player in self.playerRadiobutton:
            l = Label(framename, text="")
            l.grid(row=rowval, column=colval, columnspan=2)
            colval = colval + 2
            self.imageLabel.append(l)
        self.playername = StringVar()
        rowval = rowval + 1
        nameframe = Frame(framename)
        nameframe.grid(row=rowval, column=0)
        makeTextBox(nameframe, "Player name", self.playername, 0, 1)
        makeButton(nameframe, "Set name", self.setPlayerName, 0, 3)

    def setPlayerName(self):
        name = self.playername.get()
        player = self.choiceOfPlayer.get()
        if name == "":
            name = "Player " + str(player)
        self.playerRadiobutton[player-1].config(text=name)
        filename = config.playerNameDirectory + "Player"+str(player)+'.txt'
        writeStringToFileName(filename, name)

    def makeStageMenu(self, framename):
        '''Make radiobuttons to set the stage for each match (of the total 3 or 5)'''
        self.chosenstage = []
        self.stagebutton = []
        self.stageImageLabel = []
        self.stagechoice = IntVar()
        self.matchchoice = IntVar()
       
        self.stagechoice.set(1)
        self.matchchoice.set(5)

        self.stageChoiceWinButton = Button(framename, command=self.ShowStagesWindow, text="Choose Stage")
        self.stageChoiceWinButton.grid(row=0, column=0)
        self.stageRadiobutton = makeRadiobuttonGroup(matchNumberArray, framename, self.stagechoice, 0)
        for radio in self.stageRadiobutton:
            self.chosenstage.append(Button())
        '''Make radiobuttons for choice between Three Matcher and Five Matcher'''
        self.matchCount = makeRadiobuttonGroup(matchCountArray, framename, self.matchchoice, self.setMatches)
        rowval = 2
        colval = 0
        for match in self.stageRadiobutton:
            l = Label(framename, text="label here")
            l.grid(row=rowval, column=colval)
            colval = colval + 1
            self.stageImageLabel.append(l)

    def makeScoreTab(self, framename):
        label = Label(framename, text="otherthings")
        label.grid(row=0, column=0)


    def makeAboutTab(self, framename):
        label = Label(framename, text="Copyright-2019 VogelLover\r\nMade with love for use with SSBM\r\n"
            "To reach out to me or to read more on how to use Scoreboarder or to look at the source, go to:\n "
                "https://github.com/shrutidevasenapathy/Scoreboarder")
        label.grid(row=0, column=0)

def writeStringToFileName(filename, string):
    open(filename, 'w').close()
    file1 = open(filename, "w")
    file1.write(string)
    file1.close()