''' Copyright 2019 VogelLover '''
''' File starts Scoreboarder app'''

#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import *
import tabLayout

root = Tk()
DefaultColour = root.cget("bg")
root.wm_title(string="Scoreboarder - A customized scoreboard helper")
try:
    root.wm_iconbitmap(bitmap='samus-red.ico')
except TclError:
    print ("icon bitmap error")

tabLayout.MakeTabLayout(DefaultColour)
root.mainloop()
root.destroy
