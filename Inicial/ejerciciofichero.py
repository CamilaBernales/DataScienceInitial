class Fichero:
    def __init__(self, nombre):
        self.nombre = nombre

    def grabar_fichero(self,texto):
        fichero = open(self.nombre, "wt")
        fichero.write(texto)
        fichero.close()

    def incluir_text(self, texto):
        fichero = open(self.nombre, "at")
        fichero.write(texto)
        fichero.close()

    def leer_fichero(self):
        fichero = open(self.nombre, "rt")
        texto = fichero.read()
        return texto

