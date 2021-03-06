Copyright - 2019 VogelLover
# Scoreboarder

Simple application to assist with scoreboarding specific to SSBM. 

## How to setup ScoreBoarder: 
- Requires Python 3 (or above)
- Python packages : 
    - `pillow` Can be installed using: 
    `pip install pillow`
- Copy the contents of this repository to `<your folder>`
- Make sure that the folders in folderMap.json are pointing to the right path on your system
- Make sure that you have placed the character icons and stage icons in the right folder or
update folderMap.json to point to the correct directories
- Run Scoreboarder as `py StartScoreboarder.py` from command 
- Alternatively, Scoreboarder can be obtained as an exe (generated using `pyinstaller`). Email author for details on this.

## Folders and files required:
- Char Icons - Folder that contains all the character icons.
- Stage Icons - Folder that contains all the stage icons.
- Player input -  List of all names of player names (one in each line)
- Round input - List of all names of rounds (one in each line)
- Output - Folder that contains all outputs
- Player names - Folder that will contain text files holding player names (file will be generated by the app)
- Round names - Folder that will contain text files holding round names (file will be generated by the app)
- Score output - Folder that will contain the scores corresponding to players 1 through 4

Please help by reporting issues that you may encounter to the author


Is available for use if you credit me as "VogelLover"

Upcoming features:
- Configurability for other games/purposes.
    To be able to custom draw the app for other purposes
- Textbox that adds items to the dropdown menu for player/round names
    This will prevent having to open up the files that hold these lists and do all actions from within the app
