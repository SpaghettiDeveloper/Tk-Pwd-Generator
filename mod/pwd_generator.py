#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
from tkinter import messagebox
from tkinter.ttk import *

try:
	from tkinter import *
except:
	from Tkinter import *


master = Tk()
v = StringVar()
master.wm_title("Password generator")

# Il titolo della finestra.
b = Label(master, text="Password generator",font=("Helvetica", 32))
b.pack()

# Testo della barra di scorrimento.
z = Label(master, text="Lunghezza password",font=("Helvetica", 24))
z.pack()

# La barra di scorrimento che regola la lunghezza della password.
a = Scale(master, from_=0, to=32, orient=HORIZONTAL, length=32*10)
length = IntVar()
length.set(16)
print(a.get())
a.pack()

# Titolo del menù di scelta. 
d = Label(master, text="Tipo",font=("Helvetica", 24))
d.pack()

# Il menù di scelta.
TYPE = StringVar()
Radiobutton(master, text="Numeri", variable=TYPE, value='Numeri',font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Lettere", variable=TYPE, value="Lettere",font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Lettere e Numeri", variable=TYPE, value="Lettere e Numeri",font=("Helvetica", 24)).pack(anchor=W)
Radiobutton(master, text="Lettere, Numeri e simboli", variable=TYPE, value="Lettere, Numeri e simboli",font=("Helvetica", 24)).pack(anchor=W)
def foo():
	HELLO.set(make_password(TYPE.get(),a.get()))
	master.clipboard_clear()
	master.clipboard_append(HELLO.get())
    
def make_password(TYPE,LENGTH):
	import random
	digits = '0123456789'
	Lettere = 'abcdefghijklmnopqrstuvwxyz'
	Lettere_with_uppercase = '''abcdefghijklmnopqrstuvwxyz
	ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
	digits_and_Lettere = digits + Lettere
	all_characters = '''\1234567890'qwertyuiop+asdfghjkl<zxcvbnm,.-!"/()=?^QWERTYUIOP*ASDFGHJKLZXCVBNM;:_[]#'''
	if TYPE == 'Numeri' : TYPE = digits
	if TYPE == 'lettere' : TYPE = Lettere
	if TYPE == 'lettere e numeri' : TYPE = digits_and_Lettere
	if TYPE == 'lettere, numeri e simboli' : TYPE = all_characters     
	password = ''
	while len(password) < LENGTH:
		password = password + random.choice(TYPE)
	return(password)

# Il pulsante che genera la password.
g = Button(master, text="Genera la password", command= foo,font=("Helvetica", 14), bg = 'yellow', width=25)
g.pack()

# About
def Info():
    messagebox.showinfo("Info", "Autore: Stefano Peris")

info = Button(master, text="Info", command=Info, font=("Helvetica", 14), bg = "pink", width=25)
info.pack()

# Pulsante che chiude il programma.
def Quit():
    global master
    master.quit()

x = Button(master, text="Esci", command=Quit, font=("Helvetica", 14), bg = 'orange', width=25)
x.pack()
# ---------- Fine codice ----------

# La label (testo) all'interno del pulsante che genera la password. 
HELLO = StringVar()
w = Label(master, textvariable=HELLO,font=("Helvetica", 24))
w.pack()

# Il testo delle istruzioni.
q = Label(master, text='La password verrà copiata nella clipboard automaticamente,',font=("Helvetica", 24))
q.pack()
y = Label(master, text='Premi il tasto destro del mouse e seleziona "incolla", oppure da tastiera "CTRL-V" per incollare la password.',font=("Helvetica", 24))
y.pack()

mainloop()

