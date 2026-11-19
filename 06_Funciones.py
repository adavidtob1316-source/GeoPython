#--FUNCIONES
#Nota: ejercicios del canal de yotube @midudev

# Definir una función
print("1) Definir una función:")
#def nombre_de_la_funcion(parametro1, parametro2, ...):
  #doctring
  #Cuerpo de la función 
  #return valor_de_retorno #esto es opcional

def saludar ():
    print("Hola")

saludar()

def saludar_a(nombre):
    print(f"Hola {nombre} ¿cómo estás?")

saludar_a("Andres")
saludar_a("Julián")
saludar_a("Zara")

# Funciones con más parámetros:
print("2) Definir una función con más de un parámetro:")
def sumar(a, b):
    suma = a + b
    return suma

result = sumar(2, 3)
print(result)

#Documentar las funciones con docstring
print("3) Documentar una función con docstring:")
def restar(a, b):
    """Resta dos números y devuelve el resultado"""
    return a - b

print(restar.__doc__) #Ver el docstring

help(restar)

#Parámetros por defecto: 
print("4) Definir una función con un parámetro por defecto:")
def multiplicar (a, b = 2):
    return a * b

print(multiplicar(2))


#Argumentos de longitud variable (*args):
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1, 2, 4))
