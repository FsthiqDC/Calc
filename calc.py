from tkinter.ttk import *
import tkinter as tk
from tkinter import *

symbols = [
    "7","8","9","/","\u21BA","C","4","5","6","*","(",")","1","2","3","-","x^2","\u221A","0", ",","%","+",]

def creating_window():
    root = Tk()
    root.geometry("276x280")
    root.title("Calucator")
    root.resizable(False,False)

    return root

def creating_buttons(root):
    buttons = [Button(root, text=symbol, bg="#5b94d9", borderwidth=0, width=4, height=2) for symbol in symbols]

    j=1
    for i in range(22):
        if i % 6 == 0:
            j+=1
        buttons[i].grid(row=j, column=i%6,ipady=3, ipadx=6)

    special = Button(root, text="=", bg="#228f82",borderwidth=0, width=10, height=2)
    special.grid(row = j, column=4, columnspan=2, ipady=3, ipadx=8)

    return buttons


if __name__ == "__main__":

    root = creating_window()
    buttons = creating_buttons(root)

    root.mainloop()