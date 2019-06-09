''' Copyright 2019 VogelLover '''
''' File is used to get locations of folders, and other config elements
from folderMap.json'''

#!/usr/bin/python3

import json
from os import walk
from PIL import Image, ImageTk

with open('folderMap.json') as layoutlist:
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

charIconsDir   = configuration['Char Icons']
stageIconsDir  = configuration['Stage Icons']
playerNamesFile= configuration['Player Input']
roundNamesFile = configuration['Round Input']

outputDir      = configuration['Output']
scoresDir      = configuration['Score Output']
playerNameDir  = configuration['Player Names']
roundNameDir   = configuration['Round Names']

charImages, charImagePaths   = getAllImagesFrom(charIconsDir)
stageImages, stageImagePaths = getAllImagesFrom(stageIconsDir)
