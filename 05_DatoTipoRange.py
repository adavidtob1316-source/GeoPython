##--------DATOS TIPO RANGE
#Nota: ejercicios del canal de yotube @midudev

# Crear una secuencia o un rango de números
print("1) Crear una secuencia o un rango de números empleando la función range():")

nums = range(10) # range(inicio, fin, salto)
print(type(nums))

print(nums)

#Generar una secuencia de números:
print("2) Generar una secuencia de números empleando un bucle for y la función range():")
for num in range(5, 10):
    print(num)

for num in range(0, 10, 2):
    print(num)

for num in range(-5, 0):
    print(num)

#Cuenta regresiva:
for num in range(10, 0, -1):
    print(num)

#Crear una lista a partir del range:
print("3) Crear una lista empleando la función range():")
num = range(10)
list_nums = list(nums)
print(list_nums)

#Repetir una acción un número de veces:
print("4) Repetir una acción un número de veces empleando bucles while y for:")
contador = 0
while contador <= 5:
    print("Hacer cinco veces algo")
    contador += 1

for _ in range(5):
    print("Hacer cinco veces algo")