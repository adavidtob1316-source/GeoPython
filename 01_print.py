#---------------------------------------------------------------FUNCIÓN print()
# La función print() es el módulo que permite imprimir en la consola
print("print() permite desplegar un resultado en la consola")
print("tres", "dos", "cuatro")
# Continuar en Tipos de datos 

##--------------------------------------------------------------TIPOS DE DATOS
print(".....TIPOS DE DATOS.....")

##Enteros
print("1) Enteros:")
print("Int")
print(20)
print(-6)
print("La función type() permite consultar el tipo de dato:")
print(type(10))

#Decimales
print("2) Decimales:")
print(3.02)
print(type(9.5))

#Números complejos
print("3) Complejos:")
print(type(4+2j))

#Cadena de texto
print("4) Texto:")
print("Holiii")
print(type("Hola"))

#Booleanos
print("5) Booleanos:")
print(type(True))
print(type(1<2))

#NoneType
print("NoneType:")
print(type(None)) #Este se usa para la ausencia de valor

##----------------------------------------------------------TRANSFORMACIÓN DE DATOS
print(".....CONVERSIÓN DE TIPOS DE DATOS.....")
#De cadena de texto a entero:
print("1) De cadena de texto a entero:")
print(type(int("100")))

#De número a cadena de texto:
print("2) De entero a cadena de texto:")
print(type(str(2)))

#De cadena de texto a decimal: 
print("3) De cadena de texto a decimal:")
print(type(float("100")))

##--------------------------------------------------------------------VARIABLES
print(".....VARIABLES.....")
my_name = "Andres"
print(my_name)
#Constantes ---> Se utiliza todo en mayúscula
#Ejemplo: MI_CONSTANTE = 3.15

#Tipado de variables:
is_user_logged_in: bool = True
print(is_user_logged_in) #En configuración del editor se puede activar para chequear el tipo de variable

##-----------------------------------------------------------------FUNCIÓN input()
print(".....FUNCIÓN input().....")
nombre = input("Hola ¿ómo te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("¿Cuántos años tienes?\n")
print(f"Tu edad es {age}")