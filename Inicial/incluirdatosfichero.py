fichero = open("ficherotexto.txt", "at")
# at = añadir infomracion en modo texto
texto_fichero = "\nHola, esta es la linea que vamos a incluir en el fichero de texto"
fichero.write(texto_fichero)
fichero.close()

# cerramos el fichero