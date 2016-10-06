# -*- coding: utf-8 -*-
from Tkinter import * 
import aiml 
import tkMessageBox
v = Tk()
v.title("UPTCBOT-Ingenieria de sistemas")
v.option_add("*background", "black")
v.option_add("*foreground","white")

#k = 
k=aiml.Kernel()

def cargarCerebro():
	k.loadBrain("cerebro.brn")

text1 = Text(v, height=20, width=30)
photo=PhotoImage(file='./images/robot.gif')
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)

S = Scrollbar(v)
S.pack(side=RIGHT, fill=Y)
txt2 = Text(v, height=18, width=50)
scroll = Scrollbar(v, command=txt2.yview)
txt2.configure(yscrollcommand=scroll.set)
txt2.pack(side=TOP,fill=Y)
S.config(command=txt2.yview)
txt2.config(yscrollcommand=S.set)

cargarCerebro()

def leer(event):
	usuario="Usuario: "
	bot=">> bot: "
	pregunta=entrada.get()	
	respuesta= k.respond(pregunta)
	res=unicode(respuesta,"utf-8")
	txt2.insert(END,"\n"+usuario+pregunta+" \n")
	if (respuesta==''):
		tkMessageBox.showinfo("ATENCION!!", "La palabra no es conocida en la base del conocimiento, por favor contactar a los administradores para agregarla.")
	else:
		txt2.insert(END,"\n "+bot+respuesta+" \n")
	entrada.delete('0', END)
	txt2.see(END)
def func(event):
    leer(event)
v.bind('<Return>', leer)

	
entrada = Entry(v, bd =5,width=56)
entrada.pack(side=LEFT)

B = Button(v,text ="Enviar")
B.bind('<Button-1>', leer)
B.pack(side=RIGHT)

v.mainloop()

