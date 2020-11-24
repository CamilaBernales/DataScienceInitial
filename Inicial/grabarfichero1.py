fichero = open("fichero_para_grabar.txt", "wt")
# wt = write text
texto_fichero = "Hola, esta es la linea que vamos a grabar en el fichero de texto"
fichero.write(texto_fichero)
fichero.close() # cerramos el fichero

