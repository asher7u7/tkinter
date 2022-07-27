from tkinter import *

ventana_p = Tk()
ventana_p.title ("Grecia")
ventana_p.geometry ("800x550")
ventana_p.resizable (0,0)
ventana_p.config (bg="green")

#---------------------
#---frames banderas---
#---------------------

frame_1= Frame(ventana_p)
frame_1.config (bg="blue", width=350, height=290)
frame_1.place (x=10, y=10)

frame_2= Frame(ventana_p)
frame_2.config (bg="white", width=350, height=60)
frame_2.place (x=10, y=120)

frame_3= Frame(ventana_p)
frame_3.config (bg="white", width=60, height=290)
frame_3.place (x=150, y=10)

frame_linea1= Frame(ventana_p)
frame_linea1.config (bg="blue", width=430, height=60)
frame_linea1.place (x=360, y=10)

frame_linea2= Frame(ventana_p)
frame_linea2.config (bg="white", width=430, height=60)
frame_linea2.place (x=360, y=60)

frame_linea3= Frame(ventana_p)
frame_linea3.config (bg="blue", width=430, height=60)
frame_linea3.place (x=360, y=120)

frame_linea4= Frame(ventana_p)
frame_linea4.config (bg="white", width=430, height=60)
frame_linea4.place (x=360, y=180)

frame_linea5= Frame(ventana_p)
frame_linea5.config (bg="blue", width=430, height=60)
frame_linea5.place (x=360, y=240)

frame_linea6= Frame(ventana_p)
frame_linea6.config (bg="white", width=780, height=60)
frame_linea6.place (x=10, y=300)

frame_linea7= Frame(ventana_p)
frame_linea7.config (bg="blue", width=780, height=60)
frame_linea7.place (x=10, y=360)

frame_linea8= Frame(ventana_p)
frame_linea8.config (bg="white", width=780, height=60)
frame_linea8.place (x=10, y=420)

frame_linea9= Frame(ventana_p)
frame_linea9.config (bg="blue", width=780, height=60)
frame_linea9.place (x=10, y=480)

ventana_p.mainloop()