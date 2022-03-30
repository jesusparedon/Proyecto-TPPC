import csv

class Docente():

    def __init__(self, nombre, apellidoMaterno, apellidoPaterno, curp, materia, grupo, correo, contraseña):
        self.nom = nombre
        self.curp = curp
        self.materia = materia
        self.aP = apellidoPaterno
        self.aM = apellidoMaterno
        self.grupo = grupo
        self.correo = correo
        self.contra = contraseña

    def guardarDatos(self):

        datos = [self.nom, self.aM, self.aP, self.grupo, self.curp, self.materia, self.correo, self.contra]

        with open("datosDocente.csv", "a", newline="") as archivo:

            writer_objeto = csv.writer(archivo, delimiter=",")
            writer_objeto.writerow(datos)

    def editarDatos(nom, am, ap, curp, mate, grupo, correo, contra):
        datos=[]
        with open("datosDocente.csv", "r") as archivo:
                lector = csv.reader(archivo)
                for linea in lector:
                    if linea[6]==correo:
                        linea=[nom, am, ap, curp, mate, grupo, correo, contra]
                    datos.append(linea)

        with open("datosDocente.csv", "w", newline="") as archivo:
            writer_obj = csv.writer(archivo, delimiter=",")
            writer_obj.writerows(datos)
            

    