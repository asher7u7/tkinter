from tkinter import *

#-------------------
# ventana principal
#-------------------

ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title ("asher7u7")

#tamaño de la ventana
ventana_principal.geometry ("800x800")

#quitarle el boton de maximizar
ventana_principal.resizable(0,0)

#color de background
ventana_principal.config(bg="PaleTurquoise1")

#agregar letrero
Letrero=Label(text="\n\n\nJhoness :3",bg="PaleTurquoise1")
Letrero.pack ()

#agregar otro letrero
Letrero2=Label(text="\n\n\nSistemas <3",bg="PaleTurquoise1")
Letrero2.pack ()

#letrero 3
Letrero3=Label(text="\n\n\nColegio Guanenta",bg="PaleTurquoise1")
Letrero3.pack ()
ventana_principal.mainloop()