from tkinter import *

ventana_p2 = Tk()
ventana_p2.title ("Islandia")
ventana_p2.geometry ("800x500")
ventana_p2.resizable (0,0)
ventana_p2.config (bg="bisque")

#---------------------
#---frames banderas---
#---------------------

frame_1= Frame(ventana_p2)
frame_1.config (bg="blue", width=780, height=480)
frame_1.place (x=10, y=10)

frame_2= Frame(ventana_p2)
frame_2.config (bg="white", width=140, height=480)
frame_2.place (x=200, y=10)

frame_3= Frame(ventana_p2)
frame_3.config (bg="white", width=780, height=140)
frame_3.place (x=10, y=180)

frame_2= Frame(ventana_p2)
frame_2.config (bg="red", width=80, height=480)
frame_2.place (x=230, y=10)

frame_3= Frame(ventana_p2)
frame_3.config (bg="red", width=780, height=80)
frame_3.place (x=10, y=210)


ventana_p2.mainloop()