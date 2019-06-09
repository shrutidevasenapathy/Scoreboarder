''' Copyright 2019 VogelLover '''
''' File contains function definitions for core functionality of the Scoreboarder'''

from tkinter import *
import getConfig as config
from PIL import Image, ImageTk
import itertools
configuration = config.configuration
from functools import partial
from shutil import copy2
from FrameElements import *
import math


def writeStringToFileName(filename, string):
    ''' Write specified string to the specified filename'''
    ''' filename - name of file to hold the string '''
    ''' string - string to write to file '''
    ''' note - All contents of file are overwritten '''
    open(filename, 'w').close()
    file1 = open(filename, "w")
    file1.write(string)
    file1.close()

def reenableWindowMakingButton(window, button):
    ''' When the popup window is closed, the button used to invoke it must re-enabled'''
    ''' window - tk window element that is being closed '''
    ''' button - tk button element that invoked closing window, to be reenabled '''
    window.destroy()
    button.config(state=ACTIVE)

def setIconToLabel(labelarray, index, photo):
    ''' Add image to given label within an array of labels '''
    ''' labelarray - array containing tk label elements '''
    ''' index - index of element to which the image is to be set '''
    ''' photo - image to be set to the label element '''
    labelarray[index].config(image=photo)

def makeImageButtonGrid(framename, imgarray, patharray, action, typestring, rowval):
    ''' Create a grid of all images that will form a button array '''
    ''' framename - name of the tk frame element that is going to contain the button grid '''
    ''' imgarray - list of all images extracted from files '''
    ''' patharray - list of filenames to images '''
    ''' action - function to be called when a button is clicked '''
    ''' typestring - type of button action (e.g. stages/ player icons) to be passed on to `action` function as arg ''' 
    ''' rowval - row in the frame element where the grid is to be set '''

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
        ''' 16 Columns look good on a screen, so we limit to 16'''
        if colval == 16 :
            colval = 0
            rowval = rowval + 1

    return buttonarray

