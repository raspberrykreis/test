import Tkinter as tk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

led=GPIO.PWM(7,100)

class Aplicacion:
    def __init__(self):
        self.valor=10
        self.ventana1=tk.Tk()
        self.ventana1.title("Test PWM")
        self.label1=tk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")

        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Incrementar +10", command=self.incrementar10)
        self.boton1.grid(column=1, row=1)

        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)
        self.boton2=tk.Button(self.ventana1, text="Decrementar -10", command=self.decrementar10)
        self.boton2.grid(column=1, row=2)
        led.start(0)

        self.ventana1.mainloop()


    def incrementar(self):
        if self.valor>=100:
                self.valor=100
                led.ChangeDutyCycle(self.valor)
        else:
                self.valor=self.valor+1
                self.label1.config(text=self.valor)

    def incrementar10(self):
        self.valor=self.valor+10
        if self.valor>=100:
                self.valor=100
                led.ChangeDutyCycle(self.valor)
                self.label1.config(text=self.valor)
        else:
                
                self.label1.config(text=self.valor)

    def decrementar(self):
        if self.valor<=0:
                self.valor=0
                led.ChangeDutyCycle(self.valor)
        else:
                self.valor=self.valor-1
                self.label1.config(text=self.valor)
    def decrementar10(self):
        self.valor=self.valor-10
        if self.valor<=0:
                self.valor=0
                led.ChangeDutyCycle(self.valor)
                self.label1.config(text=self.valor)
        else:
                self.label1.config(text=self.valor)


aplicacion1=Aplicacion()
