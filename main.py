from tkinter import *
from tkinter import ttk
from dbm import *
from PIL import Image, ImageTk
import os

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CANVAS_HEIGHT = 110
CAMBRIDGE_IMAGE_HEIGHT = 100
CAMBRIDGE_IMAGE_WIDTH = 100
CAMBRIDGE_IMAGE_PATH = os.path.join(os.getcwd(),"assets/cambridge.png")
WINDOW_ICON_PATH = os.path.join(os.getcwd(),"assets/book.ico")

if __name__ == '__main__':
    root = Tk()
    root.title("")
    root.geometry(str(WINDOW_WIDTH)+'x'+str(WINDOW_HEIGHT))
    img = PhotoImage(file=WINDOW_ICON_PATH)
    root.tk.call('wm', 'iconphoto', root._w, img)
    canvas = Canvas(root,height=CANVAS_HEIGHT,width=WINDOW_WIDTH)
    canvas.pack(pady=(10,0))
    image = Image.open(CAMBRIDGE_IMAGE_PATH)
    image = image.resize((CAMBRIDGE_IMAGE_WIDTH,CAMBRIDGE_IMAGE_HEIGHT), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    canvas.create_image(WINDOW_WIDTH/2 ,CANVAS_HEIGHT/2, anchor=CENTER, image=img)
    searchLabel = ttk.Label(
        root,
        text="Search word:",
        font=('Helvetica 18 bold',12)
        , anchor="w").pack(anchor = "w",pady=(10,0))
    #searchLabel.grid(pady=(10,0),sticky = W, column=0,row=0)

    searchBox = ttk.Entry(root,width=50).pack(pady=(0,0))
    ttk.Button( text ="Search").pack()
    #searchBox.grid(column=0,row=1)
    root.mainloop()