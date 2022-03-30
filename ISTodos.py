from cgitb import text
import csv
from tkinter import *
from turtle import width

from MostrarAlumno import mostrarAlumno
from MostrarDocente import mostrarDocente

class ISTodos(Frame):

    def __init__(self, master=None, tipoUsuario=None):
        super().__init__(master)
        self.master = master
        self.config(width=400, height=300, padx=10, pady=10)
        self.pack()
        self.usu=tipoUsuario
        self.ponerTodo()

    def ponerTodo(self):
        self.labelCorreo = Label(self, text="Correo:")
        self.labelCorreo.grid(column=0, row=0, padx=8, pady=5)

        self.correo = Entry(self)
        self.correo.grid(column=1, row=0, padx=8, pady=5)

        self.labelContra = Label(self, text="Contraseña")
        self.labelContra.grid(column=0, row=1, padx=8, pady=5)

        self.contrasena = Entry(self, show="*")
        self.contrasena.grid(column=1, row=1, padx=8, pady=5)

        self.btnEntrar = Button(self, text="Iniciar sesión", command=self.Entrar)
        self.btnEntrar.grid(row=3, column=0)

        self.btnEntrar = Button(self, text="Salir", command=self.salir)
        self.btnEntrar.grid(row=3, column=1)

    def Entrar(self):
        if self.usu=="al":
            
            correo = self.correo.get()
            contra = self.contrasena.get()

            with open("datosAlumno.csv", "r") as archivo:
                lector = csv.reader(archivo)
                for linea in lector:
                    if linea[5]==correo and linea[6]==contra:
                        self.master.destroy()
                        self.al = Tk()
                        self.al.title("Alumno")

                        self.venAl = mostrarAlumno(self.al, linea)
                        self.venAl.mainloop()
                        break

        elif self.usu=="doc":

            correo = self.correo.get()
            contra = self.contrasena.get()

            with open("datosMaestros.csv", "r") as archivo:
                lector = csv.reader(archivo)
                for linea in lector:
                    if linea[6]==correo and linea[7]==contra:
                        self.master.destroy()
                        self.doc = Tk()
                        self.doc.title("Alumno")

                        self.venDoc = mostrarDocente(self.al, linea)
                        self.venDoc.mainloop()

    def salir(self):
        from escogerUsuario import ventEscoger
        self.master.destroy()
        self.esc = Tk()
        self.esc.title("Iniciar sesión")
        self.ventEsc = ventEscoger(self.esc, "IS")
