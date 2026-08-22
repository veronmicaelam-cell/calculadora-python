# 1.Definición de funciones para cada operación
def sumar(a, b):
    return a + b

def restar (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    if b == 0:
        raise ZeroDivisionError ("No se puede dividir por cero")
    return a / b

# 2.Manejo de excepciones para entradas inválidas
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: ")) 
    operacion = input("Introduce la operación (+, -, *, /): ")

    if operacion == '+': resultado = num1 + num2 
    elif operacion == '-': resultado = num1 - num2 
    elif operacion == '*': resultado = num1 * num2
    elif operacion == '/': resultado = num1 / num2 
    else: resultado = "Operación inválida" 

    print(f"El resultado es: {resultado}")

except ValueError: 
    print("Error: Por favor, ingresa un número válido")
except ZeroDivisionError as e:
    print(f"Error: {e}")

# def: Se definen sumar(), restar(), multiplicar() y dividir() de forma independiente. 

#try / except ValueError: Atrapa el error si el usuario ingresa texto en lugar de un número al 
#hacer el float().

#ZeroDivisionError: Captura el intento de dividir por cero sin que el programa falle 
#estrepitosamente.