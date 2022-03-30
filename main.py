from tkinter import *
from escogerUsuario import ventEscoger as vE

class ventPrincipal(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.config(height=200, width=200)
        self.pack()
        self.ponerTodo()

    def ponerTodo(self):
        self.btnIS = Button(self, text="Iniciar sesión", command=self.in_ses)
        self.btnIS.pack()
        self.btnIS.place(relx=0.5, anchor=CENTER, y=60)

        self.btnR = Button(self, text="Registrarse", command=self.reg)
        self.btnR.pack()
        self.btnR.place(relx=0.5, anchor=CENTER, y= 100)

    def in_ses(self):
        self.master.destroy()
        self.inSes = Tk()
        self.inSes.title("Iniciar sesión")
        self.venInSes = vE(self.inSes, "IS")
        self.venInSes.mainloop()

    def reg(self):
        self.master.destroy()
        self.regi = Tk()
        self.regi.title("Registrarse")
        self.venReg = vE(self.regi, "REG")
        self.venReg.mainloop()

ventana = Tk()
ventana.title("Registro de escuela")

ventaapp = ventPrincipal(ventana)
ventaapp.mainloop()