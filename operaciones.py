"""
Ejercicio 6 parte 1
"""

def suma():
    try:
        print('='*10,"SUMA",'='*10)
        valor1 = float(input("Ingrese el primer número: "))
        valor2 = float(input("Ingrese el segundo número: "))
        resultado = valor1 + valor2
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def resta():
    try:
        print('='*10,"RESTA",'='*10)
        valor1 = float(input("Ingrese el primer número: "))
        valor2 = float(input("Ingrese el segundo número: "))
        resultado = valor1 - valor2
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def producto():
    try:
        print('='*10,"MULTIPLICACIÓN",'='*10)
        valor1 = float(input("Ingrese el primer número: "))
        valor2 = float(input("Ingrese el segundo número: "))
        resultado = valor1 * valor2
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def division():
    try:
        print('='*10,"DIVISION",'='*10)
        valor1 = float(input("Ingrese el primer número: "))
        valor2 = float(input("Ingrese el segundo número: "))
        if valor2 == 0:
            return "Error: No es posible dividir entre cero"
        resultado = valor1 / valor2
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"
