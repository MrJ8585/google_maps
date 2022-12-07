import tkinter
from tkinter import *
from tkintermapview import TkinterMapView
#from tkintermapview import TkinterMapVie

def get_inputs():
    a = number_locations.get(1.0, END)
    b = coordenada1.get(1.0, END)
    c = coordenada2.get(1.0, END)
    d = coordenada3.get(1.0, END)
    e = coordenada4.get(1.0, END)
    return [a,b,c,d,e]

def make_array():
    out = []
    m = get_inputs()
    for i in m:
        j = i.split()
        for n in j:
            out.append(float(n))
    menu_window.destroy()
    return out

menu_window = tkinter.Tk()
menu_window.geometry(f"{400}x{500}")
menu_window.title("Menu")
menu_window.resizable(False, False)

label = Label(menu_window,text="N. de Ubicacion")
label.pack()
number_locations = tkinter.Text(menu_window, height=1, width=25, exportselection=0)
number_locations.pack()

label = Label(menu_window,text="Coordenada 1")
label.pack()
coordenada1 = tkinter.Text(menu_window, height=1, width=25, exportselection=0)
coordenada1.pack()

label = Label(menu_window,text="Coordenada 2")
label.pack()
coordenada2 = tkinter.Text(menu_window, height=1, width=25, exportselection=0)
coordenada2.pack()

label = Label(menu_window,text="Coordenada 3")
label.pack()
coordenada3 = tkinter.Text(menu_window, height=1, width=25, exportselection=0)
coordenada3.pack()

label = Label(menu_window,text="Coordenada 4")
label.pack()
coordenada4 = tkinter.Text(menu_window, height=1, width=25, exportselection=0)
coordenada4.pack()

label = Label(menu_window,text="Subir")
label.pack()
sumbmit = tkinter.Button(menu_window, height=1, width=25, command=lambda: distancia.insert(END, 1320))
sumbmit.pack()

label = Label(menu_window,text="Probando")
label.pack()
distancia = tkinter.Text(menu_window, height=1, width=25, exportselection=0)
distancia.pack()

menu_window.mainloop()