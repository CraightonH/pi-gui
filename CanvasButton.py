from tkinter import *
class CanvasButton(Canvas):
    def __init__(self, parent, width="200", height="200", color="white", command=None, text=""):
        Canvas.__init__(self, parent, borderwidth=1, highlightthickness=0)
        self.command = command
        self.configure(width=width, height=height, bg=color)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.create_text(width/2, height/2, text=text, font=("Arial", 44))

    def _on_press(self, event):
        self.configure()

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()
