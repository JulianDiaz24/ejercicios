#  Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#  captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.

try:
    ejemplo=10/0
    print("Ejecutado sin error ")
except Exception as e : 
    print(f"a ocurrido un error del tipo: .{e}")
