#!/usr/bin/env python3
from tkinter import *
import drawGUI


root = Tk()
DefaultColour = root.cget("bg")
app = drawGUI.GuiSkeleton(DefaultColour)
root.mainloop()
root.destroy
