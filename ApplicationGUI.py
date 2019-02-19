from tkinter import *

prEntryFields = []

def onCanvasConfigure(event):
    event.widget.itemconfigure("products", width=event.width)

def addMoreAction(event):
    entry = []
    for i in range(5):
        e = Entry(prListFrame)
        e.grid(row=len(prEntryFields),column=i)
        entry.append(e)
    prEntryFields.append(entry)
    prListFrame.update_idletasks()
    prListCanvas.config(scrollregion=prListFrame.bbox("all"))

keyWindow = Tk("Store Management System")

#Welcoming Label
welcomingLabel = Label(keyWindow, text="Welcome to Store Management System")
welcomingLabel.pack(side=TOP)

#Staff, Customer input and Add More frame
stctFrame = Frame(keyWindow, bg="gray")
stctFrame.pack(side=TOP, fill=X, padx=10, pady=(20,10))

staffNameLabel = Label(stctFrame, text="Staff Name")
customerIDLabel = Label(stctFrame, text="Customer ID")
addMoreLabel = Label(stctFrame, text="Add More Products")
staffNameInput = Entry(stctFrame)
customerIDInput = Entry(stctFrame)
addMoreButton = Button(stctFrame, text="+", width=10)

staffNameLabel.grid(row=0,column=0, padx=2, pady=5, sticky="w")
staffNameInput.grid(row=0,column=1, padx=2, pady=5)
customerIDLabel.grid(row=1,column=0, padx=2, pady=5, sticky="w")
customerIDInput.grid(row=1,column=1, padx=2, pady=5)
addMoreLabel.grid(row=2,column=0, padx=2, pady=5, sticky="w")
addMoreButton.grid(row=2,column=1, padx=2, pady=5)

addMoreButton.bind("<Button-1>", addMoreAction)

#Products List: frame
productsList = Frame(keyWindow, bg="red")
productsList.pack(side=TOP, fill=X)
productsList.columnconfigure(0, weight=1)
productsList.columnconfigure(1, weight=1)
productsList.columnconfigure(2, weight=1)
productsList.columnconfigure(3, weight=1)
productsList.columnconfigure(4, weight=1)

#Products List: Setting labels
prNameLabel = Label(productsList, text="Product name", width=10)
prCodeLabel = Label(productsList, text="Product Code", width=10)
prPriceLabel = Label(productsList, text="Price", width=10)
prQuantityLabel = Label(productsList, text="Quantity", width=10)
prPointsLabel = Label(productsList, text="Points", width=10)

prNameLabel.grid(row=0,column=0, ipadx=10)
prCodeLabel.grid(row=0,column=1, ipadx=10)
prPriceLabel.grid(row=0,column=2, ipadx=10)
prQuantityLabel.grid(row=0,column=3, ipadx=10)
prPointsLabel.grid(row=0,column=4, ipadx=10)

#Products List: Setting V-Scroll Canvas
prListCanvas = Canvas(productsList, height=200, bg="gray")
prListCanvas.grid(row=1,column=0,columnspan=5,stick=N+S+E+W)

vscrollbar = Scrollbar(productsList, width=20)
vscrollbar.grid(row=1,column=5,sticky=N+S)
prListCanvas.config(yscrollcommand=vscrollbar.set)
vscrollbar.config(command=prListCanvas.yview)

#Products List: Setting V-Scroll Frame
prListFrame = Frame(prListCanvas, bg="blue")
prListFrame.columnconfigure(0, weight=1)
prListFrame.columnconfigure(1, weight=1)
prListFrame.columnconfigure(2, weight=1)
prListFrame.columnconfigure(3, weight=1)
prListFrame.columnconfigure(4, weight=1)

prListCanvas.create_window((0,0), anchor=NW, window=prListFrame, tags="products")
prListFrame.update_idletasks() #REQUIRED: For f.bbox() below to work!
prListCanvas.config(scrollregion=prListFrame.bbox("all"))
prListCanvas.bind("<Configure>", onCanvasConfigure)

keyWindow.mainloop()