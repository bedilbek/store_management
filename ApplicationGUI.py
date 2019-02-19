from tkinter import *

from check import create_print_check
from initial_data import stores, staffs, customers, products, orders

keyWindow = Tk()
keyWindow.title(stores[0].name)

def create_check(event):
    create_print_check(keyWindow, orders[0])

class Hello(object):
    def __init__(self):
        print("Hello from object")

#Welcoming Label
welcomingLabel = Label(keyWindow, text=f"Welcome to {stores[0].name}")
welcomingLabel.pack(side=TOP)

#Staff, Customer input and Add More frame
stctFrame = Frame(keyWindow, bg="gray")
stctFrame.pack(side=TOP, fill=X, padx=10, pady=(20,10))

staffNameLabel = Label(stctFrame, text="Staff Name")
customerIDLabel = Label(stctFrame, text="Customer ID")
addMoreLabel = Label(stctFrame, text="Add More Products")

staffNameVar = StringVar(keyWindow)
staffNameVar.set(staffs[0].name)
staffNameOption = OptionMenu(stctFrame, staffNameVar, *[staff.name for staff in staffs])

customerIDVar = StringVar(stctFrame)
customerIDVar.set(customers[0].id)
customerIDOption = OptionMenu(stctFrame, customerIDVar, *[customer.id for customer in customers])

addMoreButton = Button(stctFrame, text="+", width=10)
addMoreButton.bind('<Button-1>', create_check)

staffNameLabel.grid(row=0,column=0, padx=2, pady=5, sticky=W)
staffNameOption.grid(row=0, column=1, padx=2, pady=5)
customerIDLabel.grid(row=1,column=0, padx=2, pady=5, sticky=W)
customerIDOption.grid(row=1, column=1, padx=2, pady=5)
addMoreLabel.grid(row=2,column=0, padx=2, pady=5, sticky=W)
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
