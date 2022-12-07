import tkinter
from tkinter import *

menu_window = tkinter.Tk()
menu_window.geometry(f"{300}x{100}")
menu_window.title("Menu")

label = Label(menu_window,text="N. de Ubicacion")
label.pack()
input = tkinter.Text(menu_window, height=1, width=15)
input.pack()

label = Label(menu_window,text="Distancia T")
label.pack()
input2 = tkinter.Text(menu_window, height=1, width=15)
input2.pack()

menu_window.mainloop()