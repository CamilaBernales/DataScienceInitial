# jSON
# convertir datos de un diccionario en estructura json

pruducto1 = {"nombre" : "silla", "color" : "blanco", "precio" : 80}

import json

estruc_json = json.dumps(pruducto1)
# print(estruc_json)

# convertir json a diccionario en python

producto2 = json.loads(estruc_json)
# print(producto2["nombre"])

# fecha y hora

from datetime import datetime

fechayhora = datetime.now()

año = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day
hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
msegundos = fechayhora.microsecond
print("la hora es {}:{}:{} y hoy es {}:{}:{}".format(hora, minutos, segundos, dia, mes, año))

# ejercicio
"""
fn buscar que mediante una expresion regular indique si una palabra esta o no en una frase
probar buscar con estas frases:
texto = "esto es una frase de pruebas para hacer busquedas"
palabra_a_buscar = "frase"
"""
import re

def buscar(palabra, texto):
    resultado = re.search(palabra, texto)
    if resultado:
        inicial = resultado.start()
        final = resultado.end()
        print("palabra encontrada, empieza en {} y termina en {}".format(inicial, final))
        return
    else:
        print("no encontrada")


texto = "Esto es una frase de pruebas para hacer busquedas"
palabra_a_buscar = "frase"

buscar(palabra_a_buscar, texto)
