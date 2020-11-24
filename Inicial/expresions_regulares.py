# expresiones regulares (search, findall, split, sub)
texto = "Hola, mi nombre es camila"
import  re

resultado = re.search("camila$", texto) # devuelve match si encuentra camila$ busca si hay una frase que acabe en camila
resultado = re.search("^Hola", texto) #^empieza con esa palaba en este caso hola (es sensible a mayus y min)
resultado = re.search("mi.*es", texto) # ente el mi y el es hay mas caractes
if(resultado):
    print("Coincidencia")
else:
    print("No hubo coincidencia")

# findall
texto = """
el coche de luis es rojo, 
el coche de antonio es blanco 
y el coche de maria es rojo
"""
resultado2 = re.findall("coche.*rojo", texto)
if(resultado2):
    print("Hay coincidencia en resultado2")
else:
    print("No hubo coincidencia")

# split => divide una cadena a partir de un patron
texto = "la silla es blanca y vale 80"
print(re.split("\s", texto)) # el caracter de corte es un caracter en blanco
# devuelve:  ['la', 'silla', 'es', 'blanca', 'y', 'vale', '80']

# sub= => sustituir coincidencias en una cadena

print(re.sub("blanca", "rosa", texto)) # la silla es rosa y vale 80
