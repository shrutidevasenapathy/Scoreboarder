''' Copyright 2019 VogelLover '''
''' File is used to get locations of folders, and other config elements
from guiLayout.json'''

#!/usr/bin/python3

import json
from os import walk
from PIL import Image, ImageTk

with open('guilayout.json') as layoutlist:
    configuration = dict(json.load(layoutlist))


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

stagesDirectory      = configuration['Stages']
destinationDirectory = configuration['OBSFolder']
scoresDirectory      = configuration['Scores']
playerNameDirectory  = configuration['Playernames']
roundNameDirectory   = configuration['Round']

charImages, charImagePaths   = getAllImagesFrom(configuration['Icons'])
stageImages, stageImagePaths = getAllImagesFrom(configuration['Stages'])
