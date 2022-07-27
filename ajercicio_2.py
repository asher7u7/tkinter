from ast import Str
from tkinter import *
from tkinter import messagebox

from numpy import empty

#funciones de la app

def sumar ():
    messagebox.showinfo("suma 1.0","Hizo click en el botón sumar...")
    c=int(a.get()) + int(b.get())
    t_resultados.insert(INSERT, "La suma de " + str(a.get()) + " + " + str(b.get()) + " es " + str(c) + "\n")

def borrar ():
    messagebox.showinfo("suma 1.0","Los datos serán borrados")
    a.set("")
    b.set("")
    t_resultados.delete("1.0","end")

def salir ():
    messagebox.showinfo("suma 1.0","La app se cerrará")
    ventana_principal.destroy()



#-------------------
# ventana principal
#-------------------

ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title ("asher7u7")

#tamaño de la ventana
ventana_principal.geometry ("800x500")

#quitarle el boton de maximizar
ventana_principal.resizable(0,0)

#color de background
ventana_principal.config(bg="black")

#----------------------
#--variables globales--
#----------------------

a=StringVar()
b=StringVar()
c=IntVar()

#-------------------
#---frame entrada---
#-------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config (bg="white", width=780, height=240)
frame_entrada.place(x=10, y=10)

#add etiqueta
titulo=Label(frame_entrada, text='Colegio San José de Guanentá')
titulo.config(bg="yellow", fg="blue", font=("Arial", 16), anchor=CENTER)
titulo.place(x=(390), y=(10))

#etiqueta subtitulo
titulo2=Label(frame_entrada, text='Especialidad en Sistemas')
titulo2.config(bg="yellow", fg="blue", font=("Arial", 12), anchor=CENTER)
titulo2.place(x=(390), y=(40))

#etiqueta subtitulo2
titulo3=Label(frame_entrada, text='Suma de dos enteros')
titulo3.config(bg="yellow", fg="blue", font=("Arial", 15), anchor=CENTER)
titulo3.place(x=(390), y=(70))

#add imagen
logo=PhotoImage(file="icono.png")
etiq_logo=Label(frame_entrada, image=logo, width=200, height=200, bg="white")
etiq_logo.place(x=(10),y=(10))

etiqueta_A=Label(frame_entrada, text='A =')
etiqueta_A.config(bg="blue", fg="black", font=("Arial", 20), anchor=CENTER)
etiqueta_A.place(x=(390), y=(120))

entry_a= Entry(frame_entrada, width=4)
entry_a.config (font=("Arial", 20), justify=CENTER, textvariable=a)
entry_a.place(x=435, y=120)

etiqueta_B=Label(frame_entrada, text='B =')
etiqueta_B.config(bg="blue", fg="black", font=("Arial", 20), anchor=CENTER)
etiqueta_B.place(x=(585), y=(120))

entry_b= Entry(frame_entrada, width=4)
entry_b.config (font=("Arial", 20), justify=CENTER, textvariable=b)
entry_b.place(x=630, y=120)

frame_operaciones= Frame(ventana_principal)
frame_operaciones.config (bg="white", width=780, height=120)
frame_operaciones.place (x=10, y=260)

bt_sumar=PhotoImage(file=("anadir.png"))
button_1=Button(frame_operaciones, image=bt_sumar, width=105, height=105, bg="White", command=sumar)
button_1.place(x=116, y=6)

bt_borrar=PhotoImage(file=("borrar.png"))
button_2=Button(frame_operaciones, image=bt_borrar, width=105, height=105, bg="White", command=borrar)
button_2.place(x=337, y=6)

bt_salir=PhotoImage(file=("salida.png"))
button_3=Button(frame_operaciones, image=bt_salir,width=105, height=105, bg="White", command=salir)
button_3.place(x=558, y=6)

frame_resultados= Frame(ventana_principal)
frame_resultados.config (bg="white", width=780, height=100)
frame_resultados.place (x=10, y=390)

#Area de texto para resultados.
t_resultados=Text(frame_resultados, width=51, height=3)
t_resultados.config(bg="green", font=("Courrier",20), fg="white")
t_resultados.pack()


ventana_principal.mainloop()