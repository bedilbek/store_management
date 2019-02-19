from tkinter import *
from typing import List
from message_dialog_box import *
from check_window import create_print_check
from initial_data import stores, staffs, customers, orders
from models.order import Order
from models.product import Product

bgColor = "#2b2b2b"
scColor = "#1f1f1f"
enColor = "#373737"
bdColor = "#7c7c7c"
font = ('Helvetica', 10)
header = ('Helvetica', 17)

keyWindow = Tk()
keyWindow.title(stores[0].name)
keyWindow.configure(background=bgColor)

prEntryFields = []
customerIDVar = None
staffNameVar = None

def create_check(event):
    if len(prEntryFields) == 0:
        showMessage("There must be at least one product!")
        return

    products = []
    try:
        for object_entry in prEntryFields:
            object_entry: List[Entry]
            products.append({
                Order.PRODUCT_KEY: Product(object_entry[1].get(), object_entry[0].get(), 'F', object_entry[2].get(), object_entry[4].get()),
                Order.QUANTITY_KEY: object_entry[3].get(),
                })
        found_customer = list(filter(lambda c: c.id == int(customerIDVar.get()), customers))[0]
        found_staff = list(filter(lambda s: s.name == staffNameVar.get(), staffs))[0]
        order = Order(stores[0], found_customer, found_staff, products)
        create_print_check(keyWindow, order)
    except (TypeError, ValueError) as e:
        showMessage(e)

def onCanvasConfigure(event):
    event.widget.itemconfigure("products", width=event.width)

def addMoreAction(event):
    entry = []
    for i in range(5):
        e = Entry(prListFrame, bg=enColor, highlightbackground=bdColor, relief=SOLID, fg="white")
        e.grid(row=len(prEntryFields),column=i,pady=2)
        entry.append(e)
    prEntryFields.append(entry)
    prListFrame.update_idletasks()
    prListCanvas.config(scrollregion=prListFrame.bbox("all"))

def addSampleProducts():
    from initial_data import products
    products: List[Product]
    for i, p in enumerate(products):
        eN = Entry(prListFrame, bg=enColor, highlightbackground=bdColor, relief=SOLID, fg="white")
        eN.insert(0, p.name)
        eN.grid(row=i,column=0,pady=2, ipady=2, ipadx = 2)
        eC = Entry(prListFrame, bg=enColor, highlightbackground=bdColor, relief=SOLID, fg="white")
        eC.insert(0, p.productCode)
        eC.grid(row=i,column=1,pady=2, ipady=2, ipadx = 2)
        eP = Entry(prListFrame, bg=enColor, highlightbackground=bdColor, relief=SOLID, fg="white")
        eP.insert(0, p.price)
        eP.grid(row=i,column=2,pady=2, ipady=2, ipadx = 2)
        eQ = Entry(prListFrame, bg=enColor, highlightbackground=bdColor, relief=SOLID, fg="white")
        eQ.insert(0, "1")
        eQ.grid(row=i,column=3,pady=2, ipady=2, ipadx = 2)
        ePo = Entry(prListFrame, bg=enColor, highlightbackground=bdColor, relief=SOLID, fg="white")
        ePo.insert(0, p.points)
        ePo.grid(row=i,column=4,pady=2, ipady=2, ipadx = 2)
        prEntryFields.append([eN, eC, eP, eQ, ePo])
    return

def showMessage(message):
    d = MessageDialogBox(keyWindow, message)
    keyWindow.wait_window(d.top)

#Welcoming Label
welcomingLabel = Label(keyWindow, text=f"Welcome to {stores[0].name}", bg=bgColor, fg="white", font=header)
welcomingLabel.pack(side=TOP)

#Staff, Customer input and Add More frame
stctFrame = Frame(keyWindow, bg=bgColor)
stctFrame.pack(side=TOP, fill=X, padx=10, pady=(20,10))

staffNameLabel = Label(stctFrame, text="Staff Name", font=font, bg=bgColor, fg="white")
customerIDLabel = Label(stctFrame, text="Customer ID", font=font, bg=bgColor, fg="white")
addMoreLabel = Label(stctFrame, text="Add More Products", font=font, bg=bgColor, fg="white")

staffNameVar = StringVar(keyWindow)
staffNameVar.set(staffs[0].name)
staffNameOption = OptionMenu(stctFrame, staffNameVar, *[staff.name for staff in staffs])
staffNameOption.config(bg=scColor, fg="white", highlightbackground=bgColor)

customerIDVar = StringVar(stctFrame)
customerIDVar.set(customers[0].id)
customerIDOption = OptionMenu(stctFrame, customerIDVar, *[customer.id for customer in customers])
customerIDOption.config(bg=scColor, fg="white", highlightbackground=bgColor )

addMoreButton = Button(stctFrame, text="+", width=10, bg=scColor, fg="white", bd=0, font=font)

staffNameLabel.grid(row=0,column=0, padx=2, pady=5, sticky=W)
staffNameOption.grid(row=0, column=1, padx=2, pady=5, sticky=W+E)
customerIDLabel.grid(row=1,column=0, padx=2, pady=5, sticky=W)
customerIDOption.grid(row=1, column=1, padx=2, pady=5, sticky=W+E)
addMoreLabel.grid(row=2,column=0, padx=2, pady=5, sticky=W)
addMoreButton.grid(row=2,column=1, padx=10, pady=5, sticky=W)

addMoreButton.bind("<Button-1>", addMoreAction)

#Products List: frame
productsList = Frame(keyWindow, bg=bgColor)
productsList.pack(side=TOP, fill=X)
productsList.columnconfigure(0, weight=1)
productsList.columnconfigure(1, weight=1)
productsList.columnconfigure(2, weight=1)
productsList.columnconfigure(3, weight=1)
productsList.columnconfigure(4, weight=1)

#Products List: Setting labels
prNameLabel = Label(productsList, text="Product name", width=10, bg=bgColor, fg="white", font=font)
prCodeLabel = Label(productsList, text="Product Code", width=10, bg=bgColor, fg="white", font=font)
prPriceLabel = Label(productsList, text="Price", width=10, bg=bgColor, fg="white", font=font)
prQuantityLabel = Label(productsList, text="Quantity", width=10, bg=bgColor, fg="white", font=font)
prPointsLabel = Label(productsList, text="Points", width=10, bg=bgColor, fg="white", font=font)

prNameLabel.grid(row=0,column=0, ipadx=10)
prCodeLabel.grid(row=0,column=1, ipadx=10)
prPriceLabel.grid(row=0,column=2, ipadx=10)
prQuantityLabel.grid(row=0,column=3, ipadx=10)
prPointsLabel.grid(row=0,column=4, ipadx=10)

#Products List: Setting V-Scroll Canvas
prListCanvas = Canvas(productsList, height=200, bg=scColor, highlightbackground=bgColor)
prListCanvas.grid(row=1,column=0,columnspan=5,stick=N+S+E+W)

vscrollbar = Scrollbar(productsList, width=15, bg=bgColor)
vscrollbar.grid(row=1,column=5,sticky=N+S)
prListCanvas.config(yscrollcommand=vscrollbar.set)
vscrollbar.config(command=prListCanvas.yview)

#Products List: Setting V-Scroll Frame
prListFrame = Frame(prListCanvas, bg=scColor, pady=5)
prListFrame.columnconfigure(0, weight=1)
prListFrame.columnconfigure(1, weight=1)
prListFrame.columnconfigure(2, weight=1)
prListFrame.columnconfigure(3, weight=1)
prListFrame.columnconfigure(4, weight=1)
prListCanvas.grid_configure(pady=5)

addSampleProducts()

prListCanvas.create_window((0,0), anchor=NW, window=prListFrame, tags="products")
prListFrame.update_idletasks() #REQUIRED: For f.bbox() below to work!
prListCanvas.config(scrollregion=prListFrame.bbox("all"))
prListCanvas.bind("<Configure>", onCanvasConfigure)
prListCanvas.itemconfigure('products', width=prListCanvas.winfo_width())

#Controls: Setting Buttons
controlsFrame = Frame(keyWindow, bg=bgColor)
controlsFrame.pack(side=TOP, fill=BOTH, expand=True)

printBtn = Button(controlsFrame, text="Print", width=15, bg=scColor, fg="white", bd=0, font=font)
closeBtn = Button(controlsFrame, text="Close", width=15, bg=scColor, fg="white", bd=0, font=font)

printBtn.pack(side=LEFT, padx=20, pady=10)
closeBtn.pack(side=LEFT, padx=20, pady=10)
closeBtn.bind("<Button-1>", lambda x: keyWindow.destroy())
printBtn.bind('<Button-1>', create_check)

#rootWindow min max size setup
keyWindow.update()
keyWindow.maxsize(keyWindow.winfo_width() + 500, keyWindow.winfo_height())
keyWindow.minsize(keyWindow.winfo_width() + 200, keyWindow.winfo_height())

keyWindow.mainloop()
