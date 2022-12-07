import tkinter
from tkintermapview import TkinterMapView

def mapa():
    main_window = tkinter.Tk()
    main_window.geometry(f"{800}x{600}")
    main_window.title("gugul mapas")

    map_widget = TkinterMapView(main_window, width=800, height=600, corner_radius=0)
    map_widget.pack(fill="both", expand=True)

    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",max_zoom=22)
    map_widget.set_address("Ensenada Baja California Mexico")

    main_window.mainloop()
