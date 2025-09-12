# Escribe un programa que intente sumar un número y una cadena. Si se produce un error
#  de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.

try:
    def sumar (a,b):
        return a+b
    operacion= sumar("casa",3)
except Exception as e:
    print(f"ocurrio un error del tipo: {e}")
    

