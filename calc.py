from tkinter.ttk import *
import tkinter as tk
from tkinter import *
from ctypes import *

final_answer = 0

symbols = [
    "7","8","9","/","\u21BA","C","4","5","6","*","(",")","1","2","3","-","^2","\u221A","0", ",","%","+"
    ]

operators = [
    "+", "*", "(", ")", "/", "%", ",", "-"
]

def creating_window():
    root = Tk()
    root.geometry("276x320")
    root.title("Calucator")
    root.resizable(False,False)

    return root

def button_click(symbol, input):
    def f():
        if symbol == "\u21BA":
            text_length = len(input.get())
            input.delete(text_length-1, END)

        elif symbol == "C":
            input.delete(0, END)

        else:
            help = len(input.get())
            last_char = input.get()

            if symbol in operators:
                if symbol != last_char[help-1]:
                    input.insert(END, symbol)
                    current_value = result.cget("text")
                    add_value = input.get()
                    new_value = current_value + add_value
                    result.config(text=new_value)
                    input.delete(0, END)
            else:
                input.insert(END, symbol)

    return f

def show_result(input, entry):
    x=2



def creating_buttons(root):
    buttons = [Button(root, text=symbol, bg="#5b94d9", borderwidth=0, width=4, height=2) for symbol in symbols]

    j=2
    for i in range(22):
        if i % 6 == 0:
            j+=1
        buttons[i].grid(row=j, column=i%6,ipady=3, ipadx=6)
        buttons[i].configure(command=button_click(symbols[i], input))

    special = Button(root, text="=", bg="#228f82",borderwidth=0, width=10, height=2, command=show_result(result, input))
    special.grid(row = j, column=4, columnspan=2, ipady=3, ipadx=8)

    return buttons

def  creating_input(root):
    result_box = Label(root, text="", anchor="w")
    result_box.grid(row = 0, columnspan=6, ipady=28)

    input_box = Entry(root)
    input_box.grid(row = 1, columnspan=6, ipadx=75, ipady=28)

    return result_box, input_box



if __name__ == "__main__":

    root = creating_window()
    result, input = creating_input(root)
    buttons = creating_buttons(root)

    root.mainloop()