from tkinter import *

raiz = Tk()
miFrame = Frame (raiz)
miFrame.pack()

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row =1, column=1, padx=10, pady=10, columnspan =4)
pantalla.config(background= "black", fg="#aeaeae", justify="right")



#---------funcion para escuchar pulsaciones

def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get()+num)


sehizo = ""
numeroguardado = ""


def guardarnumero(primernumero):
    global numeroguardado
    numeroguardado = primernumero
    numeroPantalla.set("")


def sumar(primernumero):

    guardarnumero(primernumero)

    global sehizo
    sehizo = "+"

def restar(primernumero):

    guardarnumero(primernumero)

    global sehizo
    sehizo = "-"

def multiplicar(primernumero):

    guardarnumero(primernumero)

    global sehizo
    sehizo = "*"

def dividir(primernumero):

    guardarnumero(primernumero)

    global sehizo
    sehizo = "/"





def igual():
    global numeroguardado
    global sehizo

    if sehizo == "+":
      resultado = int(numeroguardado)+int(numeroPantalla.get())
      numeroPantalla.set(resultado)
    if sehizo == "-":
      resultado = int(numeroguardado)-int(numeroPantalla.get())
      numeroPantalla.set(resultado)
    if sehizo == "*":
      resultado = int(numeroguardado)*int(numeroPantalla.get())
      numeroPantalla.set(resultado)
    if sehizo == "/":
      resultado = int(numeroguardado)/int(numeroPantalla.get())
      numeroPantalla.set(resultado)



#-----------------botones-----------------

#aca se definen los botones
button1 = Button(miFrame, text="1", width=4, command=lambda:numeroPulsado("1"))
button2 = Button(miFrame, text="2", width=4, command=lambda:numeroPulsado("2"))
button3 = Button(miFrame, text="3", width=4, command=lambda:numeroPulsado("3"))
button4 = Button(miFrame, text="4", width=4, command=lambda:numeroPulsado("4"))
button5 = Button(miFrame, text="5", width=4, command=lambda:numeroPulsado("5"))
button6 = Button(miFrame, text="6", width=4, command=lambda:numeroPulsado("6"))
button7 = Button(miFrame, text="7", width=4, command=lambda:numeroPulsado("7"))
button8 = Button(miFrame, text="8", width=4, command=lambda:numeroPulsado("8"))
button9 = Button(miFrame, text="9", width=4, command=lambda:numeroPulsado("9"))

#aca se muestran los botones por pantalla
button9.grid(row=2, column=1)
button8.grid(row=2, column=2)
button7.grid(row=2, column=3)
button6.grid(row=3, column=1)
button5.grid(row=3, column=2)
button4.grid(row=3, column=3)
button3.grid(row=4, column=1)
button2.grid(row=4, column=2)
button1.grid(row=4, column=3)

#aca se definen los botones de cuentas
buttonsumar = Button(miFrame, text="+", width=4, command=lambda:sumar(numeroPantalla.get()))
buttonrestar = Button(miFrame, text="-", width=4, command=lambda:restar(numeroPantalla.get()))
buttonmultiplicar = Button(miFrame, text="*", width=4, command=lambda:multiplicar(numeroPantalla.get()))
buttondividir = Button(miFrame, text="/", width=4, command=lambda:dividir(numeroPantalla.get()))
buttonigual = Button(miFrame, text="=", width=4, command=lambda:igual())

#aca se renderizan los botones de accion
buttonsumar.grid(row=2, column=4)
buttonrestar.grid(row=3, column=4)
buttonmultiplicar.grid(row=4, column=4)
buttondividir.grid(row=5, column=4)
buttonigual.grid(row=5, column=3)

raiz.mainloop()


