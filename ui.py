from tkinter import *
from PIL import ImageTk,Image
from tkinter.filedialog import askopenfilename

def OpenFile():
    name = askopenfilename(filetypes =(("All Files","*.*"),
                                       ("Portable Network Graphics File", "*.png"),
                                       ("Portable Network Graphics File", "*.png"),
                                       ("JPEG File", "*.jpg"),
                                       ("Graphic Interchange Format File", "*.gif")),
                           title = "Choose a file.")
    dir_loc.set(name)
    images = Image.open(name)
    hpercent = (baseheight / float(images.size[1]))
    wsize = int((float(images.size[0]) * float(hpercent)))
    images = images.resize((wsize, baseheight), Image.ANTIALIAS)
    root.img = ImageTk.PhotoImage(images)
    lb_img.configure(image=root.img)
    lb_img.update()
   
root = Tk(className=' Object Detection')
root.geometry("300x50")
btn = Button(root, text="Select an image", command=OpenFile)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
root.mainloop()
