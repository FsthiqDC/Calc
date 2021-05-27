from tkinter import font
from tkinter.ttk import *
import tkinter as tk
from tkinter import *

def text_input(text): #inputs character which was clicked by user
    userInput.insert(END, text)

def function_input(oper):
    help = len(userInput.get())
    last_char = userInput.get()

    if(oper != last_char[help-1]):
        userInput.insert(END, oper)


def remove_text(): #removing last char of input text
    textLenght = len(userInput.get())
    userInput.delete(textLenght-1, END)

def calc_result(): #result function
    x=2




root = tk.Tk()
root.title("Calc")
root.geometry("175x250")
root.resizable(False,False)

#text value
finalValue = 0
help = 0

#input
userInput = Entry(root, justify=RIGHT,state=NORMAL, cursor="arrow", )
userInput.grid(columnspan=5, row=0, pady=10, ipady=15, ipadx=20)

#OPERTATIONS ROW1
mcb = Button(root, text="MC", height=1, width=3)
mcb.grid(column=0, row=1, padx=2, pady=2)

mrb = Button(root, text="MR", height=1, width=3)
mrb.grid(column=1, row=1, padx=2, pady=2)

msb = Button(root, text="MS", height=1, width=3)
msb.grid(column=2, row=1, padx=2, pady=2)

mplusb = Button(root, text="M+", height=1, width=3)
mplusb.grid(column=3, row=1, padx=2, pady=2)

mminusb = Button(root, text="M-", height=1, width=3)
mminusb.grid(column=4, row=1, padx=2, pady=2)

#OPERATIONS ROW2
removeb = Button(root, text="←", height=1, width=3, command=lambda:remove_text())
removeb.grid(column=0, row=2, padx=2, pady=2)

ceb = Button(root, text="CE", height=1, width=3)
ceb.grid(column=1, row=2, padx=2, pady=2)

cb = Button(root, text="C", height=1, width=3)
cb.grid(column=2, row=2, padx=2, pady=2)

pmb = Button(root, text="+/-", height=1, width=3)
pmb.grid(column=3, row=2, padx=2, pady=2)

pmb = Button(root, text="√", height=1, width=3)
pmb.grid(column=4, row=2, padx=2, pady=2)

#OPERATIONS ROW3
sevenb = Button(root, text="7", height=1, width=3)
sevenb.grid(column=0, row=3, padx=2, pady=2)

eightb = Button(root, text="8", height=1, width=3)
eightb.grid(column=1, row=3, padx=2, pady=2)

nineb = Button(root, text="9", height=1, width=3)
nineb.grid(column=2, row=3, padx=2, pady=2)

divb = Button(root, text="/", height=1, width=3)
divb.grid(column=3, row=3, padx=2, pady=2)

percentb = Button(root, text="%", height=1, width=3)
percentb.grid(column=4, row=3, padx=2, pady=2)

#OPERATIONS ROW4
fourb = Button(root, text="4", height=1, width=3)
fourb.grid(column=0, row=4, padx=2, pady=2)

fiveb = Button(root, text="5", height=1, width=3)
fiveb.grid(column=1, row=4, padx=2, pady=2)

sixb = Button(root, text="6", height=1, width=3)
sixb.grid(column=2, row=4, padx=2, pady=2)

multib = Button(root, text="*", height=1, width=3,)
multib.grid(column=3, row=4, padx=2, pady=2)

equalb = Button(root, text="=", height=3, width=3, command=lambda:calc_result())
equalb.grid(column=4, row=4, rowspan=2, padx=2, pady=2)

#OPERATION ROW5
oneb = Button(root, text="1", height=1, width=3, command=lambda:text_input('1'))
oneb.grid(column=0, row=5, padx=2, pady=2)

twob = Button(root, text="2", height=1, width=3,command=lambda:text_input('2'))
twob.grid(column=1, row=5, padx=2, pady=2)

threeb = Button(root, text="3", height=1, width=3,command=lambda:text_input('3'))
threeb.grid(column=2, row=5, padx=2, pady=2)

minusb = Button(root, text="-", height=1, width=3, command=lambda:function_input('-'))
minusb.grid(column=3, row=5, padx=2, pady=2)

#OPERATIONS ROW6
zerob = Button(root, text="0", height=1, width=8)
zerob.grid(column=0,columnspan=2, row=6, padx=2, pady=2)

threeb = Button(root, text=",", height=1, width=3)
threeb.grid(column=2, row=6, padx=2, pady=2)

minusb = Button(root, text="+", height=1, width=3)
minusb.grid(column=3, row=6, padx=2, pady=2)

emptyb = Button(root,text="...", height=1, width=3 )
emptyb.grid(column=4, row=6, padx=2, pady=2)



root.mainloop()