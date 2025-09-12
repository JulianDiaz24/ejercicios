# Escribe un programa que intente acceder a una clave que no existe en un
#  diccionario. Si se produce una excepción KeyError, captura la excepción y muestra

try:
    diccionario = {"nombre": "Lautaro", "edad": 2}
    print(diccionario["apellido"])
except Exception as e :
    print(f"che salio mal, fijate: {e}")
    