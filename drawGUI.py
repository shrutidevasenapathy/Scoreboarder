from tkinter import *
import getConfig as config
from PIL import Image, ImageTk
import itertools
configuration = config.configuration
from functools import partial
from shutil import copy2
from FrameElements import *


class GuiSkeleton():
    def __init__(self, DefaultColour):
        self.defaultColor = DefaultColour
        matchgridrow       = 0
        stagechoicegridrow = 1
        stageimagegridrow  = 2
        playergridrow      = 3
        playernamegridrow  = 4
        charsgridrow       = 5


        self.matchframe       = makeFrameInRow(matchgridrow)
        self.stageimageframe  = makeFrameInRow(stageimagegridrow)
        self.stagechoiceframe = makeFrameInRow(stagechoicegridrow)
        self.playerframe      = makeFrameInRow(playergridrow)
        self.charsframe       = makeFrameInRow(charsgridrow)
        self.playernameframe  = makeFrameInRow(playernamegridrow)

        '''Make match numbers radiobuttons'''
        #Create a variable that acts as the "group" indicator for radiobuttons related to a given choice
        self.matchchoice = IntVar()
        self.matchchoice.set(5)
        self.matchCount = makeRadiobuttonGroup(configuration['match_count'], self.matchframe, self.matchchoice, self.setMatches)

        # Make all stage radiobuttons
        self.stagechoice = IntVar()
        self.stagechoice.set(1)
        self.stageRadiobutton = makeRadiobuttonGroup(configuration['stagenumber'], self.stagechoiceframe, self.stagechoice, self.highlightChosenStage)
        self.chosenstage = []
        for radio in self.stageRadiobutton:
            self.chosenstage.append(Button())

        # Make all player radiobuttons
        self.playerchoice = IntVar()
        self.playerchoice.set(1)
        self.playerRadiobutton = makeRadiobuttonGroup(configuration['playernumber'], self.playerframe, self.playerchoice, self.highlightChosenChar)
        self.chosencharacter = []
        for radio in self.playerRadiobutton:
            self.chosencharacter.append(Button()) 

        #Make all stage icons into a row of buttons
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
        makeButton(self.playernameframe, "Set", self.setPlayerName, 0, 2)
        makeTextBox(self.playernameframe, "Player name", self.playername, 0, 1)
        '''self.playernamelabel = Label(self.playernameframe, text="Player Name")
        self.playernamelabel.grid(row=0, column=1)
        
        Entry(self.playernameframe, textvariable=self.playername).grid(row=0, column=2)
        Button(self.playernameframe, text="Set", command=self.setPlayerName).grid(row=0, column=3)'''


        #Make all characters icons into a grid of buttons
        self.charimg = []
        self.charbutton = []
        rowval = charsgridrow
        colval = 0
        buttoncount = 0
        for img in config.charImages:
            self.charimg.append(ImageTk.PhotoImage(img))
        for photo, path in itertools.zip_longest(self.charimg, config.charImagePaths):
            b = Button(self.charsframe, image=photo, command=partial(self.copytodestinationwithname, path, "player",self.playerchoice, buttoncount), activebackground='grey')
            buttoncount = buttoncount + 1
            self.charbutton.append(b)
            b.grid(row=rowval, column=colval)
            colval = colval + 1
            if colval == 15 :
                colval = 0
                rowval = rowval + 1 
    
    def setPlayerName(self):
        name = self.playername.get()
        player = self.playerchoice.get()
        if name== "":
            name = "Player " + str(player)
        self.playerRadiobutton[player-1].config(text=name)
        filename = "Player"+str(player)+'.txt'
        open(filename, 'w').close()
        file1 = open(filename, "w")
        file1.write(name)
        file1.close()

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