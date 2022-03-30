from tkinter import *

class mostrarDocente(Frame):

    def __init__(self, master=None, linea=None):
        super().__init__(master)
        self.master = master
        self.config(width=300, height=300)
        self.pack()
        self.linea = linea
        self.ponerTodo()

    def ponerTodo(self):
        self.nomTxt = Label(self, text="Nombre: "+self.linea[0])
        self.nomTxt.grid(column=0, row=0, padx=8, pady=5)
        
        self.aPTxt = Label(self, text="Apellido paterno: "+self.linea[1])
        self.aPTxt.grid(column=0, row=1, padx=8, pady=5)

        self.aMTxt = Label(self, text="Apellido materno: "+self.linea[2])
        self.aMTxt.grid(column=0, row=2, padx=8, pady=5)

        self.mateTxt = Label(self, text="Grupo: "+self.linea[3])
        self.mateTxt.grid(column=0, row=3, padx=8, pady=5)

        self.grupoTxt = Label(self, text="Curp: "+self.linea[4])
        self.grupoTxt.grid(column=0, row=4, padx=8, pady=5)

        self.curpTxt = Label(self, text="Materia: "+self.linea[5])
        self.curpTxt.grid(column=0, row=5, padx=8, pady=5)

        self.correoTxt = Label(self, text="Correo: "+self.linea[6])
        self.correoTxt.grid(column=0, row=6, padx=8, pady=5)

        self.btnSalir = Button(self, text="Salir", command=self.salir)
        self.btnSalir.grid(column=0, row=6, padx=8, pady=5)

    def salir(self):
        self.master.destroy()
        from ISTodos import ISTodos
        self.IS = Tk()
        self.IS.title("Iniciar sesión")

        self.venIS = ISTodos(self.IS)
        self.venIS.mainloop()