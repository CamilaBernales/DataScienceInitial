"""
ejercicio:
1) crear clase coche y funcion lambda media
"""

class Coche:
    def __init__(self, marca, color, combustible, cilindradas):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindradas = cilindradas

    def mostrar(self):
        print(f" \n Marca: {self.marca} \n Color: {self.color} \n Combustible: {self.combustible} \n Cilindradas: {self.cilindradas}")


media = lambda nota1, nota2, nota3 : (nota1 + nota2 + nota3) / 3