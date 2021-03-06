''' Copyright 2019 VogelLover '''
''' File starts Scoreboarder app'''

#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import *
import tabLayout

root = Tk()
DefaultColour = root.cget("bg")
root.wm_title(string="Scoreboarder")
try:
    root.wm_iconbitmap(bitmap='favicon.ico')
except TclError:
    print ("favicon error")

tabLayout.MakeTabLayout(DefaultColour)
root.resizable(width=False, height=False)
root.mainloop()
root.destroy
