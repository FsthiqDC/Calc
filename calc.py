import tkinter as tk
from tkinter.constants import ANCHOR, BOTTOM

root = tk.Tk()
root.title("Calculator")
root.geometry("220x280")
root.resizable(False,False)

root.columnconfigure(0, pad=3)
root.columnconfigure(1, pad=3)
root.columnconfigure(2, pad=3)
root.columnconfigure(3, pad=3)

root.rowconfigure(0, pad=3)
root.rowconfigure(1, pad=3)
root.rowconfigure(2, pad=3)
root.rowconfigure(3, pad=3)
root.rowconfigure(4, pad=3)

#////


mr.pack()

root.mainloop()