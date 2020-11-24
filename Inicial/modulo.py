import camelcase

camel = camelcase.CamelCase()
texto = "mi nombre es camila"
print(camel.hump((texto)))
# Mi Nombre Es Camila


#funciones que importamos en programa

def saludar(nombre):
    print("Hola soy " + nombre)

def desperdirse(nombre):
    print("Adios " + nombre)


