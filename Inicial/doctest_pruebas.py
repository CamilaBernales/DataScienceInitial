# doctest => generar pruebas dentro de la documentacion
def sumar(num1, num2):
    """
    >>> sumar(4,3)
    7
    """
    return num1 + num2

resultado = sumar(4,3)
print(resultado)

import doctest
doctest.testmod()