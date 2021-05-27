from tkinter.ttk import *
import tkinter as tk
from tkinter import *

symbols = [
    "7","8","9","/","\u21BA","C","4","5","6","*","(",")","1","2","3","-","x^2","\u221A","0", ",","%","+",]

def creating_window():
    root = Tk()
    root.geometry("276x320")
    root.title("Calucator")
    root.resizable(False,False)

    return root

def button_click(text_box, symbol):
    def f():
        if symbol == "\u21BA":
             textLenght = len(text_box.get())
             text_box.delete(textLenght-1, END)

        elif symbol == "C":
            text_box.delete(0, END)

        else:
            text = symbol if symbol != "x^2" else "^2"
            text_box.insert(END, text)

    return f


def creating_buttons(root):
    buttons = [Button(root, text=symbol, bg="#5b94d9", borderwidth=0, width=4, height=2) for symbol in symbols]

    j=2
    for i in range(22):
        if i % 6 == 0:
            j+=1
        buttons[i].grid(row=j, column=i%6,ipady=3, ipadx=6)
        buttons[i].configure(command=button_click(text_box, buttons[i]["text"]))

    special = Button(root, text="=", bg="#228f82",borderwidth=0, width=10, height=2)
    special.grid(row = j, column=4, columnspan=2, ipady=3, ipadx=8)

    return buttons

def user_input(root):
    input_box = Entry(root, borderwidth=0, background="#ffffff")
    input_box.grid(row=2, columnspan=6, ipadx=76, ipady=25)

    result_box = Label(root, background="#ffffff")
    result_box.grid(row=1, columnspan=6, ipadx=134, ipady=30)
    return input_box, result_box



if __name__ == "__main__":

    root = creating_window()
    text_box, info = user_input(root)
    buttons = creating_buttons(root)

    root.mainloop()