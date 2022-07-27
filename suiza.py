from tkinter import *

pestaña_p3= Tk()
pestaña_p3.config(bg="SlateBlue2")
pestaña_p3.geometry("500x500")
pestaña_p3.resizable(0,0)
pestaña_p3.title("Suiza")

#---------------------
#---frames banderas---
#---------------------

frame_1=Frame(pestaña_p3)
frame_1.config(bg="red", width=480, height=480)
frame_1.place(x=10, y=10)

frame_2=Frame(pestaña_p3)
frame_2.config(bg="white", width=160, height=480)
frame_2.place(x=170, y=10)

frame_3=Frame(pestaña_p3)
frame_3.config(bg="white", width=480, height=160)
frame_3.place(x=10, y=170)

pestaña_p3.mainloop()