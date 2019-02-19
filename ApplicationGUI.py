from tkinter import *

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

#Products List frame
productsList = Frame(keyWindow, bg="red")
productsList.pack(side=TOP, fill=X)
productsList.columnconfigure(0, weight=1)
productsList.columnconfigure(1, weight=1)
productsList.columnconfigure(2, weight=1)
productsList.columnconfigure(3, weight=1)
productsList.columnconfigure(4, weight=1)

prNameLabel = Label(productsList, text="Product name")
prCodeLabel = Label(productsList, text="Product Code")
prPriceLabel = Label(productsList, text="Price")
prQuantityLabel = Label(productsList, text="Quantity")
prPointsLabel = Label(productsList, text="Points")

prNameLabel.grid(row=0,column=0)
prCodeLabel.grid(row=0,column=1)
prPriceLabel.grid(row=0,column=2)
prQuantityLabel.grid(row=0,column=3)
prPointsLabel.grid(row=0,column=4)

#Bottom Controls
controls = Frame(keyWindow)
controls.pack(side=TOP, fill=BOTH)



keyWindow.mainloop()