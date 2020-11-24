import ejerciciofichero as moduloFichero

nombre_fichero  = 'ejercicioFichero.text'
fichero = moduloFichero.Fichero(nombre_fichero)

texto = "esta es la segunda fila del fichero"
fichero.grabar_fichero(texto)

texto = "esta es la linea que voy a incluir"
fichero.incluir_text(texto)

fichero_leido = fichero.leer_fichero()
print(fichero_leido)