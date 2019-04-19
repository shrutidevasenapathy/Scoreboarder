''' Copyright 2019 VogelLover '''
''' File starts Scoreboarder app'''

#!/usr/bin/env python3
from tkinter import *
import Coreboarder


root = Tk()
DefaultColour = root.cget("bg")
app = Coreboarder.DrawScoreboarder(DefaultColour)
root.mainloop()
root.destroy
