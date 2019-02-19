import tkinter as tk
from tkinter import Tk, StringVar
from tkinter.ttk import Frame

from models.order import Order

def onCanvasConfigure(event):
    event.widget.itemconfigure("products", width=event.width)


def create_print_check(root: Tk, order: Order):
    check_window = tk.Toplevel(root)
    general_info_frame = Frame(check_window, padding=(0, 0, 0, 0))
    general_info_frame.pack(side= tk.TOP)
    tk.Label(general_info_frame, text='Welcome to ' + order.storeObject.name, justify=tk.CENTER, font=('Helvetica', 20)).pack(pady=10)
    tk.Label(general_info_frame, text='Staff Name: \t' + order.staffObject.name, justify=tk.LEFT, font=('Helvetice', 11)).pack(anchor=tk.W, padx=0)
    tk.Label(general_info_frame, text='Customer ID: \t' + str(order.customerObject.id), justify=tk.LEFT, font=('Helvetice', 11)).pack(anchor=tk.W, padx=0)

    # Products List frame
    productsList = tk.Frame(check_window, bd=1, relief=tk.SUNKEN)
    productsList.pack(side=tk.TOP, fill=tk.X)
    productsList.columnconfigure(0, weight=1)
    productsList.columnconfigure(1, weight=1)
    productsList.columnconfigure(2, weight=1)
    productsList.columnconfigure(3, weight=1)
    productsList.columnconfigure(4, weight=1)

    prNameLabel = tk.Label(productsList, text="Product name", width=15, font=('Helvetica', 11, 'bold'))
    prCodeLabel = tk.Label(productsList, text="Product Code", width=15, font=('Helvetica', 11, 'bold'))
    prPriceLabel = tk.Label(productsList, text="Price", width=15, font=('Helvetica', 11, 'bold'))
    prQuantityLabel = tk.Label(productsList, text="Quantity", width=15, font=('Helvetica', 11, 'bold'))
    prPointsLabel = tk.Label(productsList, text="Points", width=15, font=('Helvetica', 11, 'bold'))

    prNameLabel.grid(row=0, column=0)
    prCodeLabel.grid(row=0, column=1)
    prPriceLabel.grid(row=0, column=2)
    prQuantityLabel.grid(row=0, column=3)
    prPointsLabel.grid(row=0, column=4)

    # Products List: Setting V-Scroll Canvas
    prListCanvas = tk.Canvas(productsList, height=80)
    prListCanvas.grid(row=1, column=0, columnspan=5, stick=tk.N + tk.S + tk.E + tk.W)

    vscrollbar = tk.Scrollbar(productsList, width=15)
    vscrollbar.grid(row=1, column=5, sticky=tk.N + tk.S)
    prListCanvas.config(yscrollcommand=vscrollbar.set)
    vscrollbar.config(command=prListCanvas.yview)

    # Products List: Setting V-Scroll Frame
    prListFrame = tk.Frame(prListCanvas)
    prListFrame.columnconfigure(0, weight=1)
    prListFrame.columnconfigure(1, weight=1)
    prListFrame.columnconfigure(2, weight=1)
    prListFrame.columnconfigure(3, weight=1)
    prListFrame.columnconfigure(4, weight=1)

    for index, product in enumerate(order.productObjects):
        tk.Label(prListFrame, width=15, text=product.name).grid(row=index, column=0)
        tk.Label(prListFrame, width=15, text=product.productCode).grid(row=index, column=1)
        tk.Label(prListFrame, width=15, text=product.price).grid(row=index, column=2)
        tk.Label(prListFrame, width=15, text=order.quantity[index]).grid(row=index, column=3)
        tk.Label(prListFrame, width=15, text=product.points).grid(row=index, column=4)

    prListCanvas.create_window((0, 0), anchor=tk.NW, window=prListFrame, tags="products")
    prListFrame.update_idletasks()  # REQUIRED: For f.bbox() below to work!
    prListCanvas.config(scrollregion=prListFrame.bbox("all"))
    prListCanvas.bind("<Configure>", onCanvasConfigure)
    prListCanvas.itemconfigure('products', width=prListCanvas.winfo_width())

    total_cost = sum([product.price*order.quantity[index] for index, product in enumerate(order.productObjects)])
    total_points = sum([product.points*order.quantity[index] for index, product in enumerate(order.productObjects)])

    order_footer_info = Frame(check_window, padding=(50, 20, 0, 20))
    order_footer_info.pack(side=tk.TOP, fill=tk.X)
    tk.Label(order_footer_info, text=f'Total: \t\t{total_cost}', font=('Helvetica', 11)).pack(anchor=tk.W)
    tk.Label(order_footer_info, text=f'Total Items: \t{sum(order.quantity)}', font=('Helvetica', 11)).pack(anchor=tk.W)
    tk.Label(order_footer_info, text=f'Points: \t\t{total_points}', font=('Helvetica', 11)).pack(anchor=tk.W)

    cancel_btn = tk.Button(check_window, text="Cancel", width=15)
    cancel_btn.pack(side=tk.RIGHT, padx=10, pady=10)
    cancel_btn.bind('<Button-1>', lambda x: check_window.destroy())

    #rootWindow min max size setup
    check_window.update()
    check_window.maxsize(check_window.winfo_width() + 100, check_window.winfo_height())
    check_window.minsize(check_window.winfo_width(), check_window.winfo_height())






