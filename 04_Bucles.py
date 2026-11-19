##------------------------------------------------BUCLES 
#Nota: ejercicios del canal de yotube @midudev

##-----------------------------------BUCLES WHILE
print("--------------------------BUCLES WHILE")

#------Bucle con una simple condición
print("1) Bucle con una condición simple:")
contador = 0
while contador <= 5:
    print(contador)
    contador += 1 #Bucle para que el programa cuente hasta 5

#Ejemplo de bucle infinito:
#while True:
    #print("Hola") 

#Romper el buble con la palabra break:

print("\n 2) Bucle while con break:")
contador = 0
while True: 
    print(contador)
    contador += 1
    if contador == 5:
        break # sale del bucle apenas llegue a 5

#Bucle con la palabra continue. Lo que hace es saltar una iteración en concreto:
print("\n3) Bucle con continue para saltarse un dato:")
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)

#------Bucle con una cindición else

print("\n4) Bucle con condición else:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1 
else:
    print("El bucle ha terminado")

#El else asegura que la condición es falsa revisando cada una de las iteraciones

#------Ejemplo práctico con un bucle while

#Pedirle al usuario un número que tiene que ser positivo
#Si no, no le dejamos en paz

numero = -1
while numero < 0:
  try: #El try-except permite controlar excepciones o errores que terminarían con el programa
    numero = int(input("Escribe un número positivo:")) #int transforma la cadena de texto en entero
    if numero < 0:
        print("El número debe ser positivo. Intenta de nuevo.")
  except:
    print("Intenta otra vez.")

print(f"El número que has introducido es {numero}") #La f formatea cadenas de texto para evaluar números adentro



##-----------------------------------BUCLES FOR
print("-------------------------BUCLES FOR")

frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
   print(fruta)

cadena = "midudev"
for caracter in cadena: 
   print(caracter)

#-----Emplear Enumerate para enumerar propiedades de la lista
print("1) Emplear Enumerate para enumerar propiedades de la lista:")

frutas = ["manzana", "pera", "mandarina"]
for index, fruta in enumerate (frutas):
   print(f"El índice es {index} y la fruta es {fruta}")

#-----Bucles for anidados 
print("2) Bucles for anidados:")

letras =["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras: 
   for numero in numeros:
      print(f"{letra}{numero}")

#-----Uso de Break 
print("3) Emplear el break para terminar el bucle:")

animales = ["loro", "pez", "canario", "pato", "perro"]
for animal in animales: 
   print(animal)
   if animal == "canario":
      break

animales = ["loro", "pez", "canario", "pato", "perro"]
for index, animal in enumerate(animales): 
   print(animal)
   if animal == "canario":
      print(f"El canario está escondido en el índice {index}")
      break
   
#-----Uso de continue
print("4) Emplear el continue para saltarse un dato:")

animales = ["loro", "pez", "canario", "pato", "perro"]
for index, animal in enumerate(animales): 
   if animal == "canario":
      continue
   print(animal)
