# Escribe un programa que intente dividir dos números. Si el segundo número es cero,
#  captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
#  captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.



def dividamos(a,b):   
    try:
        resultado = a / b
        print(resultado)
    except TypeError:
        print(f"Ambos operadores deben ser numericos")
        dividamos(10,5)
    except ZeroDivisionError:
        print(f"El divisor no puede ser 0")
        dividamos(10,"asd")

dividamos(10,0)