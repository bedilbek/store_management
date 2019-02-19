import tkinter as tk
from tkinter import Tk, StringVar
from tkinter.ttk import Frame

from models import Order


def create_print_check(root: Tk, order: Order):
    check_window = tk.Toplevel(root)
    general_info_frame = Frame(check_window, padding="30 30 30 30")
    general_info_frame.pack()
    tk.Label(general_info_frame, text='Welcome to ' + order.storeObject.name, justify=tk.CENTER).pack()

    tk.Label(general_info_frame, text='Staff Name: \t' + order.staffObject.name, justify=tk.LEFT).pack(anchor=tk.W)

    tk.Label(general_info_frame, text='Customer Name: \t' + order.customerObject.name, justify=tk.LEFT).pack(anchor=tk.W)

    # Products List frame
    productsList = tk.Frame(check_window, bg="red")
    productsList.pack(side=tk.TOP, fill=tk.X)
    productsList.columnconfigure(0, weight=1)
    productsList.columnconfigure(1, weight=1)
    productsList.columnconfigure(2, weight=1)
    productsList.columnconfigure(3, weight=1)
    productsList.columnconfigure(4, weight=1)

    prNameLabel = tk.Label(productsList, text="Product name", width=15)
    prCodeLabel = tk.Label(productsList, text="Product Code", width=15)
    prPriceLabel = tk.Label(productsList, text="Price", width=15)
    prQuantityLabel = tk.Label(productsList, text="Quantity", width=15)
    prPointsLabel = tk.Label(productsList, text="Points", width=15)

    prNameLabel.grid(row=0, column=0)
    prCodeLabel.grid(row=0, column=1)
    prPriceLabel.grid(row=0, column=2)
    prQuantityLabel.grid(row=0, column=3)
    prPointsLabel.grid(row=0, column=4)






