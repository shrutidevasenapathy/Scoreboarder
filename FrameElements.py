''' Copyright 2019 VogelLover '''
''' File contains implementation of some tkinter frame elements 
 that are used more than once in Coreboarder'''

from tkinter import *

'''Definition of radiobuttons for three/five matcher choice'''
matchCountArray = [
    {"label":"Three Matcher", "row":"0", "column":"2", "value":"3"},
    {"label":"Five Matcher",  "row":"0", "column":"4", "value":"5"}
    ]

'''Definition of radiobuttons for players'''
playerNumberArray = [
    {"label": "Player 1", "row":"1", "column":"0", "value":"1" },
    {"label": "Player 2", "row":"1", "column":"2", "value":"2" },
    {"label": "Player 3", "row":"1", "column":"4", "value":"3" },
    {"label": "Player 4", "row":"1", "column":"6", "value":"4" }
]

'''Definition of radiobuttons for match number choice'''
matchNumberArray = [
    {"label": "Match 1", "row":"1", "column":"0", "value":"1" },
    {"label": "Match 2", "row":"1", "column":"1", "value":"2" },
    {"label": "Match 3", "row":"1", "column":"2", "value":"3" },
    {"label": "Match 4", "row":"1", "column":"3", "value":"4" },
    {"label": "Match 5", "row":"1", "column":"4", "value":"5" }
]

def makeFrameTab(widget):
    newframe = Frame(widget)
    return newframe

def makeFrameInRow(rownum):
    newframe = Frame()
    newframe.grid(row=rownum)
    return newframe

'''Create radiobuttons, make sure you assign the same variable for the whole group. This indicates that a choice is made between them
Give them different values. Assign an on-click action with "command" '''
def makeRadiobuttonGroup(configarray, frame, groupvar, action):
    radiobuttonlist = []
    for radiobuttonconfig in configarray:
        rb = Radiobutton(frame, text = radiobuttonconfig["label"], variable=groupvar, value=radiobuttonconfig["value"], command=action)
        rb.grid(row=radiobuttonconfig["row"], column=radiobuttonconfig["column"])
        radiobuttonlist.append(rb)
    return radiobuttonlist

def makeTextBox(frame, textlabel, textvar, rowval, colval):
    labelname = Label(frame, text=textlabel)
    labelname.grid(row=rowval, column=colval)
    Entry(frame, textvariable=textvar).grid(row=rowval, column=colval+1)

def makeButton(frame, buttonlabel, command, rowval, colval):
    button = Button(frame, text=buttonlabel, command=command)
    button.grid(row=rowval, column=colval)
    return button
