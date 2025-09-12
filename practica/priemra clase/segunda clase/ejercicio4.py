#  Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
#  FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
#  embargo, también intenta crear el archivo si no existe.


try:
    # Intentamos abrir un archivo en modo lectura
    with open("archivo_inexistente.txt", "r") as f:
        contenido = f.read()
        print("Contenido del archivo:", contenido)

except FileNotFoundError:
    print("Error: El archivo no existe.")


    # Si no existe, lo creamos en modo escritura
    with open("archivo_inexistente.txt", "w") as f:
        f.write("Este archivo fue creado porque no existía.\n")
    print("Archivo creado con éxito.")