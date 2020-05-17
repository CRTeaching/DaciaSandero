# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:12:23 2020

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:02:31 2020
@author: USER
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter.filedialog import askopenfilename
import os

root = Tk(className=' Object Detection')

def OpenFile():
    name = askopenfilename(initialdir=os.getcwd(),
                           filetypes =(("All Files","*.*"),
                                       ("Portable Network Graphics File", "*.png"),
                                       ("Portable Network Graphics File", "*.png"),
                                       ("JPEG File", "*.jpg"),
                                       ("Graphic Interchange Format File", "*.gif")),
                           title = "Choose a file.")
    if not name:
        return
     # setup new window for
    new_window = Toplevel(root)
    im = Image.open(name)
    # load image
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(new_window,image = tkimage)
    myvar.image = tkimage
    myvar.pack()





root.geometry("300x50")
btn = Button(root, text="Select an image", command=OpenFile)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
root.mainloop()
