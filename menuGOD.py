import tkinter as tk                    
from tkinter import ttk
from tkintermapview import TkinterMapView

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
ttk.tkinter.Text(tab1, height=1, width=25, exportselection=0).pack()

ttk.Label(tab1,text="Coordenada 1").pack()
coordenada1 = ttk.tkinter.Text(tab1, height=1, width=25, exportselection=0)
coordenada1.pack()

ttk.Label(tab1,text="Coordenada 2").pack()
coordenada2 = ttk.tkinter.Text(tab1, height=1, width=25, exportselection=0)
coordenada2.pack()

ttk.Label(tab1,text="Coordenada 3").pack()
coordenada3 = ttk.tkinter.Text(tab1, height=1, width=25, exportselection=0)
coordenada3.pack()

ttk.Label(tab1,text="Coordenada 4").pack()
coordenada4 = ttk.tkinter.Text(tab1, height=1, width=25, exportselection=0)
coordenada4.pack()

ttk.Label(tab1,text="Subir").pack()
sumbmit = ttk.tkinter.Button(tab1, height=1, width=25)
sumbmit.pack()


#Map
map_widget = TkinterMapView(tab2, width=800, height=600, corner_radius=0)
map_widget.pack(fill="both", expand=True)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
map_widget.set_address("Ensenada Baja California Mexico")

root.mainloop()

