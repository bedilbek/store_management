from tkinter import *

class MessageDialogBox:
    def __init__(self, parent, message):
        top = self.top = Toplevel(parent)
        Label(top, text=message).pack(padx=20,pady=20)
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        self.top.destroy()