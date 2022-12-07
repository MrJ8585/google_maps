import tkinter as tk                    
from tkinter import ttk
from tkintermapview import TkinterMapView
import functions

#funcion que no se donde poner ayuda
def get_inputs():
    a = locations.get(1.0, tk.END)
    b = coordenada1.get(1.0, tk.END)
    c = coordenada2.get(1.0, tk.END)
    return [a,b,c]

def make_array():
    out = []
    m = get_inputs()
    for i in m:
        j = i.split()
        for n in j:
            out.append(float(n))
    for i in range(int(out[0])):
        functions.node(out[1], out[3], out[2], out[4])

#Set UP
root = tk.Tk()
root.geometry(f"{800}x{600}")
root.title("Tab Widget")
tabControl = ttk.Notebook(root)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Inputs')
tabControl.add(tab2, text ='Map')
tabControl.pack(expand = 1, fill ="both")


#Tab de inputs
ttk.Label(tab1,text="N. de Ubicacion").pack()
locations = ttk.tkinter.Text(tab1, height=1, width=25, exportselection=0)
locations.pack()

ttk.Label(tab1,text="Coordenada 1").pack()
coordenada1 = ttk.tkinter.Text(tab1, height=1, width=25, exportselection=0)
coordenada1.pack()

ttk.Label(tab1,text="Coordenada 2").pack()
coordenada2 = ttk.tkinter.Text(tab1, height=1, width=25, exportselection=0)
coordenada2.pack()

ttk.Label(tab1,text="Subir").pack()
sumbmit = ttk.tkinter.Button(tab1, height=1, width=25, command=make_array)
sumbmit.pack()


#Map
map_widget = TkinterMapView(tab2, width=800, height=600, corner_radius=0)
map_widget.pack(fill="both", expand=True)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
map_widget.set_address("Ensenada Baja California Mexico")

root.mainloop()

