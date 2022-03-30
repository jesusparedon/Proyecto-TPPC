import csv
from tkinter import *
from tkinter import messagebox
from turtle import width

from click import command

from editarAlumno import EA
from editarDocente import ED

class ventAdmin(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.config(width=200, height=200, padx=10, pady=10)
        self.pack()
        self.ponerTodo()

    def ponerTodo(self):
        self.btnCA = Button(self, text="Consultar alumnos", command=self.CA)
        self.btnCA.grid(column=0, row=0, padx=8, pady=5)

        self.btnCD = Button(self, text="Consultar docentes", command=self.CD)
        self.btnCD.grid(column=1, row=0, padx=8, pady=5)

        self.btnEA = Button(self, text="Editar alumnos", command=self.EA)
        self.btnEA.grid(column=0, row=1, padx=8, pady=5)

        self.btnED = Button(self, text="Editar docentes", command=self.ED)
        self.btnED.grid(column=1, row=1, padx=8, pady=5)

        self.btnSalir = Button(self, text="Salir", command=self.salir)
        self.btnSalir.grid(column=0, row=2, padx=8, pady=5, columnspan=2)

    def CA(self):
        with open("datosAlumno.csv", "r") as archivo:
            lector = csv.reader(archivo)
            lineaFF=""
            for linea in lector:
                lineaF=""
                for campo in linea:
                    lineaF = lineaF+campo+" "
                lineaFF=lineaFF+lineaF+"\n"
        messagebox.showinfo("Consultando Alumnos", lineaFF)

    def CD(self):
        with open("datosDocente.csv", "r") as archivo:
            lector = csv.reader(archivo)
            lineaFF=""
            for linea in lector:
                lineaF=""
                for campo in linea:
                    lineaF = lineaF+campo+" "
                lineaFF=lineaFF+lineaF+"\n"
        messagebox.showinfo("Consultando Docentes", lineaFF)

    def EA(self):
        self.master.destroy()
        self.EA = Tk()
        self.EA.title("Editar alumnos")

        self.ventEA = EA(self.EA)
        self.ventEA.mainloop()

    def ED(self):
        self.master.destroy()
        self.ED = Tk()
        self.ED.title("Editar docentes")

        self.ventED = ED(self.ED)
        self.ventED.mainloop()

    def salir(self):
        from escogerUsuario import ventEscoger
        self.master.destroy()

        self.esc = Tk()
        self.esc.title("Iniciar sesión")
        self.ventEsc = ventEscoger(self.esc, "IS")
        self.ventEsc.mainloop()