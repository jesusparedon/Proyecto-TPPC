from tkinter import *
from tkinter import messagebox
from Docente import Docente

class ED(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.config(width=300, height=500)
        self.pack()
        self.ponerTodo()

    def ponerTodo(self):
        self.nomTxt = Label(self, text="Nombre")
        self.nomTxt.grid(column=0, row=0, padx=8, pady=5)
        
        self.aPTxt = Label(self, text="Apellido paterno")
        self.aPTxt.grid(column=0, row=1, padx=8, pady=5)

        self.aMTxt = Label(self, text="Apellido materno")
        self.aMTxt.grid(column=0, row=2, padx=8, pady=5)

        self.mateTxt = Label(self, text="Materia")
        self.mateTxt.grid(column=0, row=3, padx=8, pady=5)

        self.grupoTxt = Label(self, text="Grupo:")
        self.grupoTxt.grid(column=0, row=4, padx=8, pady=5)

        self.curpTxt = Label(self, text="Curp")
        self.curpTxt.grid(column=0, row=5, padx=8, pady=5)

        self.correoTxt = Label(self, text="Correo:")
        self.correoTxt.grid(column=0, row=6, padx=8, pady=5)

        self.contraTxt = Label(self, text="Contraseña:")
        self.contraTxt.grid(column=0, row=7, padx=8, pady=5)

        self.nom = Entry(self)
        self.nom.grid(column=1, row=0, padx=8, pady=5)

        self.aP = Entry(self)
        self.aP.grid(column=1, row=1, padx=8, pady=5)

        self.aM = Entry(self)
        self.aM.grid(column=1, row=2, padx=8, pady=5)

        self.mate = Entry(self)
        self.mate.grid(column=1, row=3, padx=8, pady=5)

        self.grupo = Entry(self)
        self.grupo.grid(column=1, row=4, padx=8, pady=5)
        
        self.curp = Entry(self)
        self.curp.grid(column=1, row=5, padx=8, pady=5)

        self.correo = Entry(self)
        self.correo.grid(column=1, row=6, padx=8, pady=5)

        self.contra = Entry(self, show="*")
        self.contra.grid(column=1, row=7, padx=8, pady=5)

        self.info = Label(self, text="Para editar, introduzca\nlos nuevos datos pero\nmanteniendo el correo anterior")
        self.info.grid(column=0, row=8, padx=8, pady=5, columnspan=2)

        self.btnSalida = Button(self, text="Salir", command=self.salir)
        self.btnSalida.grid(column=0, row=9, padx=8, pady=5)

        self.btnRegistrarse = Button(self, text="Registrarse", command=self.Editar)
        self.btnRegistrarse.grid(column=1, row=9, padx=8, pady=5)

    def salir(self):
        from ventanaAdministrador import ventAdmin
        self.master.destroy()
        self.ISad = Tk()
        self.ISad.title("Administrador")
        self.venISad = ventAdmin(self.ISad)
        self.venISad.mainloop()

    def Editar(self):
        
        curp = self.curp.get()
        nom = self.nom.get()
        ap = self.aP.get()
        am = self.aM.get()
        grupo = self.grupo.get()
        correo = self.correo.get()
        contra = self.contra.get()
        mate = self.mate.get()

        doc = Docente.editarDatos(nom, am, ap, curp, mate, grupo, correo, contra)

        messagebox.showinfo("Hecho", "Tarea completada, información actualizada")