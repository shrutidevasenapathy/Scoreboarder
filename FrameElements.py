''' Copyright 2019 VogelLover '''
''' File contains implementation of some tkinter frame elements 
 that are used more than once in Coreboarder'''

from tkinter import *
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
