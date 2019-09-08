from tkinter import *
from CanvasButton import *
import stoplightAPI

SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100

def createMainMenu(parent):
    clear(parent)
    btnRed = CanvasButton(parent, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, color="blue", text="Stoplight Controls", command=lambda: createStoplightMenu(parent, createMainMenu))
    btnYellow = CanvasButton(parent, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, color="purple", text="Purple")
    btnGreen = CanvasButton(parent, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, color="white", text="White")
    btnNegative = CanvasButton(parent, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, color="orange", text="Exit", command=quit)
    btnRed.grid(row=0,column=0)
    btnYellow.grid(row=0,column=1)
    btnGreen.grid(row=1,column=0)
    btnNegative.grid(row=1,column=1)

def createStoplightMenu(parent, callback):
    clear(parent)
    btnRed = CanvasButton(parent, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, color="red", text="Red", command=stoplightAPI.setRed)
    btnYellow = CanvasButton(parent, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, color="yellow", text="Yellow", command=stoplightAPI.setYellow)
    btnGreen = CanvasButton(parent, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, color="green", text="Green",command=stoplightAPI.setGreen)
    btnNegative = CanvasButton(parent, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, color="orange", text="Back", command=lambda: callback(parent))
    btnRed.grid(row=0,column=0)
    btnYellow.grid(row=0,column=1)
    btnGreen.grid(row=1,column=0)
    btnNegative.grid(row=1,column=1)

def clear(parent):
    #parent.delete("all")
    items = root.grid_slaves()
    for i in items:
        i.destroy()

def setFullscreenApp():
    root = Tk()
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    SCREEN_WIDTH = root.winfo_screenwidth()
    SCREEN_HEIGHT = root.winfo_screenheight()
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(SCREEN_WIDTH, SCREEN_HEIGHT))
    root.focus_set()  # <-- move focus to this widget
    return root

if __name__ == "__main__":
    root = setFullscreenApp()
    createMainMenu(root)
    root.mainloop()

