import os
os.system("clear")

#Nota: ejercicios del canal de yotube @midudev
###------------------------------------------------------------SENTENCIAS CONDICIONALES
print(".....SENTENCIAS CONDICIONALES.....")
print("\n Sentencia simple condicional")
edad = 18
if edad >= 18:
    print("Eres mayor de edad")

print("\n Sentencia simple condicional con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


print("\n Sentencia simple condicional con elif")
nota = 1
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Perdiste")

###--------------------------------------------------------------OPERADORES LÓGICOS
print(".....OPERADORES LÓGICOS.....")
print("\n Condiciones múltiples")

## AND
print("1) Operador AND:")
edad = 20
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else: 
    print("Estás arrestado")

# Se tienen que cumplir las dos condiciones 

## OR
print("2) Operador OR:")
if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else: 
    print("Estás arrestado")
#Una de las dos condiciones tiene que ser verdadera

## Negar la condición 
print("3) Operador NOT:")
es_fin_de_semana = True
if not es_fin_de_semana:
    print("Qué mal")
else:
    print("Qué bien")

#-----------------------------------------Anidar condicionales 
print(".....CONDICIONAL ANIDADO.....")
edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes entrar a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("Eres muy pequeño")

##-----------Tablas de verdad 

print("\nTablas de verdad:")
print("AND:")
print("  A      B       A and B")
print("True   True   ", True and True)
print("True   False  ", True and False)
print("False  True   ", False and True)
print("False  False  ", False and False)

print(" ")
print("OR:")
print("  A      B       A or B")
print("True   True   ", True or True)
print("True   False  ", True or False)
print("False  True   ", False or True)
print("False  False  ", False and False)


numero = 5
if numero:
    print("El número no es cero")

numero = 0 
if numero:
    print("Aquí no entrará nunca")

nombre = "Juan"
if nombre:
    print("El nombre no es vacío")


##-----------------------------------------------------------------CONDICIÓN TERNARIA

print("\n Condición ternaria:")

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)
