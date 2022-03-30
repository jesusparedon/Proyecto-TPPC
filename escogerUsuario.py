from tkinter import *

from ISTodos import ISTodos
from REGAlumno import registrarAlumno
from REGDocente import registrarDocente
from ventanaAdministrador import ventAdmin

class ventEscoger(Frame):

    def __init__(self, master=None, queEscogio=None):
        super().__init__(master)
        self.master= master
        self.qEsco = queEscogio
        self.config(width=200, height=240)
        self.pack()
        self.ponerTodo()

    def ponerTodo(self):
        self.btnAL = Button(self, text="Alumno", command=self.al)
        self.btnAL.pack()
        self.btnAL.place(relx=0.5, anchor=CENTER, y=60)

        self.btnD = Button(self, text="Docente", command=self.doc)
        self.btnD.pack()
        self.btnD.place(relx=0.5, anchor=CENTER, y=100)

        if self.qEsco=="IS":
            self.btnAD = Button(self, text="Administrador", command=self.ad)
            self.btnAD.pack()
            self.btnAD.place(relx=0.5, anchor=CENTER, y=140)

        self.salida = Button(self, text="Salir", command=self.salir)
        self.salida.pack()
        self.salida.place(relx=0.2, y=180)

    def al(self):
        if self.qEsco == "IS":
            self.master.destroy()
            self.IS = Tk()
            self.IS.title("Alumno")
            self.venIS = ISTodos(self.IS, "al")
            self.venIS.mainloop()
        elif self.qEsco == "REG":
            self.master.destroy()
            self.REGAl = Tk()
            self.REGAl.title("Alumno")
            self.venREG = registrarAlumno(self.REGAl)
            self.venREG.mainloop()

    def doc(self):
        if self.qEsco == "IS":
            self.master.destroy()
            self.IS = Tk()
            self.IS.title("Docente")
            self.venIS = ISTodos(self.IS, "doc")
            self.venIS.mainloop()
        elif self.qEsco == "REG":
            self.master.destroy()
            self.REGDoc = Tk()
            self.REGDoc.title("Alumno")
            self.venREG = registrarDocente(self.REGDoc)
            self.venREG.mainloop()

    def ad(self):
        self.master.destroy()
        self.ISad = Tk()
        self.ISad.title("Administrador")
        self.venISad = ventAdmin(self.ISad)
        self.venISad.mainloop()

    def salir(self):
        self.master.destroy()
        from main import ventPrincipal
        ventana = Tk()
        ventana.title("Registro de escuela")

        ventaapp = ventPrincipal(ventana)
        ventaapp.mainloop()

