import csv

class Alumno():

    def __init__(self, nombre, apellidoMaterno, apellidoPaterno, grupo, boleta, correo, contraseña):
        self.bol = boleta
        self.nom = nombre
        self.aP = apellidoPaterno
        self.aM = apellidoMaterno
        self.grupo = grupo
        self.correo = correo
        self.contra = contraseña

    def guardarDatos(self):

        datos = [self.nom, self.aM, self.aP, self.grupo, self.bol, self.correo, self.contra]

        with open("datosAlumno.csv", "a", newline="") as archivo:

            writer_objeto = csv.writer(archivo, delimiter=",")
            writer_objeto.writerow(datos)

    def editarDatos(nom, am, ap, grupo, bol, correo, contra):
      datos=[]
      with open("datosAlumno.csv", "r") as archivo:
            lector = csv.reader(archivo)
            for linea in lector:
                if linea[5]==correo:
                    linea=[nom, am, ap, grupo, bol, correo, contra]
                datos.append(linea)

      with open("datosAlumno.csv", "w", newline="") as archivo:
          writer_obj = csv.writer(archivo, delimiter=",")
          writer_obj.writerows(datos)


    