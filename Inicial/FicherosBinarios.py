# pickle - modulo para grabas ficheros bianarios
import pickle
"""lista_colores = ["azul", "verde", "rojo", "amarillo"]
fichero = open("fichero_colores.pckl", "wb")
pickle.dump(lista_colores, fichero) # grabo en binario la lista de colores en el fichero
fichero.close()"""

"""#leerlo
fichero = open("fichero_colores.pckl", "rb")
lista_leida = pickle.load(fichero)
print(lista_leida) # devuelve el array"""

# ejercicio

"""
crear dicc frutas = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}
grabar estructuras de deatos frutas como un fichero binario
recuperar estructura de datos 
verificar que sigue siendo un diccionari ejecuntando el metodo values()
"""
frutas = {"manzana" : "apple", "naranja" : "orange", "platano" : "banana", "limon" : "lemon"}
fichero = open("frutas_archivo.pckl", "wb")
pickle.dump(frutas, fichero)
fichero.close()

# leerlo
fichero2 = open("frutas_archivo.pckl", "rb")
fichero_leido = pickle.load(fichero2)
print(fichero_leido.values())