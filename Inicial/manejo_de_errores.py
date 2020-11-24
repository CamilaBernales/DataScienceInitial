"""try:
    numero1 = 5
    numero2 = 3
    div = numero1 / numero2
    print(div)
except ZeroDivisionError:
    print("No puedes dividir por cero")
except:
    print("Ha ocurrido un error")
else:
    print("La division funciono correctamente") # cuando funciona
finally:
    print("Estamos aprendiendo excepctiones") # siempre se muestra"""

# ejercicio
"""
crear la fn "operacion" que dados 3 num, divida el primer numero entre la resta de los otros dos numeros
utilizar la fn creado con los nmeros 5,4,2
utilizar la fn creada con los numeros 6,3,3
"""
def operacion(num1, num2, num3):
    try:
        operacion_matematica = num1 / (num2 - num3)
        print(operacion_matematica)
    except:
        print("Hubo un error, revise si esta ingresando los dos ultimos dos numeros con el mismo valor y/o esta dividiendo en cero :/ ")
    else:
        print("Operacion realizada con exito")
    finally:
        print("La operacion ha terminado")

operacion(5,4,4)
