import tkinter
from tkinter import *

menu_window = tkinter.Tk()
menu_window.geometry(f"{300}x{150}")
menu_window.title("Menu")
menu_window.resizable(False, False)

def save_text():
   text_file = open("archivo.txt", "w")
   text_file.write(input.get(1.0, END))
   text_file.close()

label = Label(menu_window,text="N. de Ubicacion")
label.pack()
input = tkinter.Text(menu_window, height=1, width=15)
input.pack()
save = Button(text="Aceptar", command=save_text)
save.pack()

def save_text2():
   text_file = open("archivo2.txt", "w")
   text_file.write(input.get(1.0, END))
   text_file.close()

label = Label(menu_window,text="Distancia T")
label.pack()
input2 = tkinter.Text(menu_window, height=1, width=15)
input2.pack()
save2 = Button(text="Aceptar", command=save_text2)
save2.pack()

menu_window.mainloop()