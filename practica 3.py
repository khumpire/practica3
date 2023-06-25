# """Problema 1"""

def calcular_porcentaje_fraccion(fraccion):
    numerador, denominador = fraccion
    porcentaje = (numerador / denominador) * 100

    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return f'{round(porcentaje)}%'


def ingresar_fraccion():
    while True:
        fraccion = input("Ingresa una fracción en formato X/Y: ")
        partes = fraccion.split("/")
        if len(partes) == 2:
            try:
                numerador = int(partes[0])
                denominador = int(partes[1])
                if numerador >= denominador and denominador != 0:
                    return numerador, denominador
                else:
                    print("Error: X debe ser mayor o igual a Y, y Y no puede ser cero.")
            except ValueError:
                print("Error: Los valores ingresados no son números enteros.")
        else:
            print("Error: Formato de fracción inválido.")


while True:
    try:
        fraccion = ingresar_fraccion()
        resultado = calcular_porcentaje_fraccion(fraccion)
        print("La cantidad de combustible en el tanque es:", resultado)
        break
    except ValueError as e:
        print(f"Error: {str(e)}")
    except ZeroDivisionError as e:
        print("Error: El denominador no puede ser cero.")

"""Problema 2"""
calificaciones = input("Ingrese una lista de calificaciones separadas por comas: ")
lista_calificaciones = calificaciones.split(',')
calificaciones_enteros = []
for calificacion in lista_calificaciones:
    try:
        calificacion_entero = int(calificacion)
        calificaciones_enteros.append(calificacion_entero)
    except ValueError:
        print(f"Error: La calificación '{calificacion}' no es un número válido.")

print("Calificaciones en enteros:", calificaciones_enteros)

"""Problema 3"""
def triangulo_de_pascal(n):
    if n <= 0:
        print("El número de filas debe ser mayor que cero.")
        return

    triángulo = []
    for i in range(n):
        fila = [1] * (i + 1)
        for j in range(1, i):
            fila[j] = triángulo[i - 1][j - 1] + triángulo[i - 1][j]
        triángulo.append(fila)

    for fila in triángulo:
        print(' '.join(map(str, fila)))
n_filas=int(input("Ingrese filas "))
triangulo_de_pascal(n_filas)

"""Problema 4"""
def longitud_ultima_palabra(string):
    
    string = string.strip()        
    palabras = string.split()        
    if len(palabras) > 0:       
        ultima_palabra = palabras[-1]
        return len(ultima_palabra)
    else:     
        return 0
palabra=input("Ingrese un texto: ")
longitud = longitud_ultima_palabra(palabra)
print("Longitud de la última palabra:", longitud)



