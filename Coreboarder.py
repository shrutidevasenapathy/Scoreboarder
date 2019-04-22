''' Copyright 2019 VogelLover '''
''' File contains core functionality of the Scoreboarder'''

from tkinter import *
import getConfig as config
from PIL import Image, ImageTk
import itertools
configuration = config.configuration
from functools import partial
from shutil import copy2
from FrameElements import *
import math

# This implements the entire structure and functionality of
# the scoreboarder app.
"""
class DrawScoreboarder():
    def __init__(self, DefaultColour):

        self.defaultColor = DefaultColour       # used to clear a custom colour setting

        # Each gridrow is a frame in the grid. This way we force different grid layouts 
        matchgridrow       = 0
        stagechoicegridrow = 1
        stageimagegridrow  = 2
        playergridrow      = 3
        playernamegridrow  = 4
        scoregridrow       = 5
        charsgridrow       = 6
        roundnamegridrow   = 7

        self.matchframe       = makeFrameInRow(matchgridrow)
        self.stagechoiceframe = makeFrameInRow(stagechoicegridrow)
        self.stageimageframe  = makeFrameInRow(stageimagegridrow)
        self.playerframe      = makeFrameInRow(playergridrow)
        self.playernameframe  = makeFrameInRow(playernamegridrow)
        self.scoreframe       = makeFrameInRow(scoregridrow)
        self.charsframe       = makeFrameInRow(charsgridrow)
        self.roundnameframe   = makeFrameInRow(roundnamegridrow)

        '''Make radiobuttons for choice between Three Matcher and Five Matcher'''
        #Create a variable that acts as the "group" indicator for radiobuttons related to a given choice
        self.matchchoice = IntVar()
        self.matchchoice.set(5)
        self.matchCount = makeRadiobuttonGroup(configuration['match_count'], self.matchframe, self.matchchoice, self.setMatches)

        '''Make radiobuttons to set the stage for each match (of the total 3 or 5)'''
        self.stagechoice = IntVar()
        self.stagechoice.set(1)
        self.stageRadiobutton = makeRadiobuttonGroup(configuration['stagenumber'], self.stagechoiceframe, self.stagechoice, self.highlightChosenStage)
        self.chosenstage = []
        for radio in self.stageRadiobutton:
            self.chosenstage.append(Button())

        '''Make radiobuttons to choose the player number to configure (allows setting name, score, character)'''
        self.playerchoice = IntVar()
        self.playerchoice.set(1)
        self.playerRadiobutton = makeRadiobuttonGroup(configuration['playernumber'], self.playerframe, self.playerchoice, self.highlightChosenChar)
        self.chosencharacter = []
        self.playerscore = []
        for radio in self.playerRadiobutton:
            self.chosencharacter.append(Button())
            self.playerscore.append(0)


        '''Make a grid of buttons to set stage icon for selected match (selected using match radio button)'''
        self.localcopy_stageimage = []
        rowval = stageimagegridrow
        colval = 0
        stagebuttoncount = 0
        self.stagebutton = []
        for img in config.stageImages:
            img = img.resize((50,50))
            self.localcopy_stageimage.append(ImageTk.PhotoImage(img))
        for photo, path in itertools.zip_longest(self.localcopy_stageimage, config.stageImagePaths):
            x = Button(self.stageimageframe, image=photo, command=partial(self.copytodestinationwithname, path, "stage", self.stagechoice, stagebuttoncount), activebackground='grey')
            stagebuttoncount = stagebuttoncount + 1
            x.grid(row=rowval, column=colval)
            self.stagebutton.append(x)
            colval = colval + 1
            if colval == 12 :
                colval = 0
                rowval = rowval + 1
        
        self.playername = StringVar()
        makeTextBox(self.playernameframe, "Player name", self.playername, 0, 1)
        makeButton(self.playernameframe, "Set name", self.setPlayerName, 0, 3)

        Label(self.scoreframe, text="Set Score").grid(row=0, column=1)
        makeButton(self.scoreframe, "Score +", self.upScore, 0, 2)
        makeButton(self.scoreframe, "Score -", self.downScore, 0, 3)

        self.roundname = StringVar()
        makeTextBox(self.roundnameframe, "Round name", self.roundname, 0, 1)
        makeButton(self.roundnameframe, "Set name", self.setRoundName, 0, 3)

        '''Make a grid of buttons to set character icon for selected player (selected using player radio button)'''
        self.charimg = []
        self.charbutton = []
        rowval = charsgridrow
        colval = 0
        buttoncount = 0
        rowval = rowval + 1
        for img in config.charImages:
            self.charimg.append(ImageTk.PhotoImage(img))
        for photo, path in itertools.zip_longest(self.charimg, config.charImagePaths):
            b = Button(self.charsframe, image=photo, command=partial(self.copytodestinationwithname, path, "player",self.playerchoice, buttoncount), activebackground='grey')
            buttoncount = buttoncount + 1
            self.charbutton.append(b)
            b.grid(row=rowval, column=colval)
            colval = colval + 1
            if colval == 16 :
                colval = 0
                rowval = rowval + 1 
    def upScore(self):
        player = self.playerchoice.get()
        score = self.playerscore[player-1]
        score = score + 1
        if score > self.matchchoice.get():
            score = self.matchchoice.get()
        self.playerscore[player-1] = score
        filename = config.scoresDirectory + "Score"+str(player)+".txt"
        self.writeStringToFileName(filename, str(score))

    def downScore(self):
        player = self.playerchoice.get()
        score = self.playerscore[player-1]
        score = score - 1
        if score < 0 :
            score = 0
        self.playerscore[player-1] = score
        filename = config.scoresDirectory + "Score"+str(player)+".txt"
        self.writeStringToFileName(filename, str(score))


    def writeStringToFileName(self, filename, string):
        open(filename, 'w').close()
        file1 = open(filename, "w")
        file1.write(string)
        file1.close()

    def setPlayerName(self):
        name = self.playername.get()
        player = self.playerchoice.get()
        if name == "":
            name = "Player " + str(player)
        self.playerRadiobutton[player-1].config(text=name)
        filename = config.playerNameDirectory + "Player"+str(player)+'.txt'
        self.writeStringToFileName(filename, name)
    
    def setRoundName(self):
        roundname = self.roundname.get()
        filename = config.roundNameDirectory + "Roundname.txt"
        self.writeStringToFileName(filename, roundname)

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
            self.chosenstage[choice.get()-1] = self.stagebutton[count]
            self.highlightChosenStage()
        copy2(path, config.destinationDirectory + filenamepart + str(choice.get()) + ".png")
    #Highlight the chosen character with a coloured box around the character icon button
    def highlightChosenChar(self):
        player = self.playerchoice.get()
        for button in self.charbutton:
            button['background'] = self.defaultColor
        self.chosencharacter[player-1]['background'] = 'blue'
        self.playername.set("")

    #Highlight the chosen character with a coloured box around the character icon button
    def highlightChosenStage(self):
        stage = self.stagechoice.get()
        for button in self.stagebutton:
            button['background'] = self.defaultColor
        self.chosenstage[stage-1]['background'] = 'red'

    #Set the number of matches for the Stages display
    def setMatches(self):
        self.matchesCount = self.matchchoice.get()
        if self.matchesCount == 3:
            self.stagechoice.set(1)
            self.stageRadiobutton[3]['state'] ="disabled"
            self.stageRadiobutton[4]['state'] ="disabled"
            copy2(config.stagesDirectory+"default.png", config.destinationDirectory + "stage4.png")
            copy2(config.stagesDirectory+"default.png", config.destinationDirectory + "stage5.png")
        else:
            self.stageRadiobutton[3]['state'] ="normal"
            self.stageRadiobutton[4]['state'] ="normal"
"""

def writeStringToFileName(filename, string):
    open(filename, 'w').close()
    file1 = open(filename, "w")
    file1.write(string)
    file1.close()

def popupWindowCloseAction(window, button):
    window.destroy()
    button.config(state=ACTIVE)

def setIconToLabel(labelarray, index, photo):
    labelarray[index].config(image=photo)

def makeImageButtonGrid(framename, imgarray, patharray, action, typestring):
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