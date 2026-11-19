#Nota: ejercicios del canal de yotube @midudev

## LISTAS

print("\nCrear listas")
#-----------------------------------------------------------------TIPOS DE LISTAS
print("\n------TIPOS DE LISTAS")

print("\n1) Lista de enteros")
lista1 = [1, 2, 3, 4, 5]
print(lista1)

print("\n2) Lista de flotantes")
lista2 = [1.3, 2.0, 3.5, 4.8, 5.1]
print(lista2)

print("\n3) Lista de cadenas")
lista3 = ["manzanas", "peras", "bananos"]
print(lista3)

print("\n4) Lista mixta")
lista4 = [5.5, 1, "bananos"]
print(lista4)

print("\n5) Lista vacía")
lista5 = []
print(lista5)

print("\n6) Lista de listas")
lista6 = [[1, 2], [3, 4]]
print(lista6)

print("\n7) Matriz")
lista7 = [[1, 2], [2, 3], [3, 4]]
print(lista7)

#---------Restringir el tipo de dato 
print("\n------RESTRINGIR EL TIPO DE DATO DE UNA LISTA")
Lista8: list[int]  = [1, 2, 3, 4, 5] #Para esta lista solo son válidos los datos tipo entero


#------------------------------------------------ACCEDER A ELEMENTOS DE UNA LISTA POR EL ÍNDICE
print("\n------------------ACCEDER A ELEMENTOS DE UNA LISTA POR EL ÍNDICE")
print(lista3[0]) #Acceder de acuerdo a la posición en la lista (empezando por 0 porque es la primera posición)
print(lista3[-1]) #Acceder al índice desde el último elemento (negativo)

##----------Acceder a elementos por índice en una matriz
print(lista7[0][1]) #Dentro del primer corchete se especifica la posición de la lista macro y en el segundo, la posición específica dentro de la lista micro
   
##----------Modificar elementos en una lista 
print("\n--------------------MODIFICAR ELEMENTOS EN UNA LISTA")
#Para modificar elmentos en una lista, primero se convierten en variable:
lista1[0] = 20
print(lista1)

##----------------------------------------------------------AÑADIR ELEMENTOS A UNA LISTA
print("-----------------------AÑADIR ELEMENTOS A UNA LISTA")
#------Primer método: concatenación:
print("1) Método de concatenación")
lista1 = lista1 + [4, 5, 6]
print(lista1)

#-----Segundo método: modifica directamente la lista
print("2) Modificar directamente la lista empleando +=")
lista1 += [7, 8, 9]
print(lista1)

##----------Recuperar la longitud de una lista 
print("-----------------------------------INDAGAR LA LONGITUD DE UNA LISTA")
print(len(lista1))


##--------------------------------------------------------------MÉTODOS DE LAS LISTAS
print("----------------------------------------MÉTODOS DE LAS LISTAS")
print("1) Añador un elemento al final de la lista con .append()")
lista1.append(6) # Añade un elemento al final de la lista
print(lista1)

lista1 = ["a", "b", "c", "d"]
print("2) Insertar un elemento en la posición indicada como primer parámetro con .insert()")
lista1.insert(1, "Q") #Inserta un elemento en la posición que le indiquemos como primer parámetro
print(lista1)

print("3) Agregar un elemento al final de la lista con .extend()")
lista1.extend("Z") #Agrega elementos al final de la lista
print(lista1)

##------------------------------------------------------------ELIMINAR ELEMENTOS DE LA LISTA

print("---------------------------------------ELIMINAR ELEMENTOS DE LA LISTA")
lista1 = ["a", "b", "c", "d"]
print("1) Eliminar la primera aparición del elemento indicado con .remove()")
lista1.remove("a") #Elimina la primera aparición del elemnto indicado
print(lista1)

print("2) Eliminar el último elemento de la lista y mostrarlo con .pop()")
lista1.pop() #Elimina el último elemento de la lista y además lo devuelve
print(lista1)

lista1 = ["a", "b", "c", "d"]
print("3) Eliminar el elemento del índice indicado con .pop()")
lista1.pop(1) #Elimina el elemento del índice indicado (índice 1 en este caso)
print(lista1)

print("4) Eliminar todos los elementos de la lista con .clear()")
lista1.clear() #Elimina todos los elemntos de la lista
print(lista1)

lista1 = ["a", "b", "c", "d"]
print("5) Eliminar un rango de elementos con del nombre_lista[a:b]")
del lista1[1:3] #Elimina el rango de elementos indicado
print(lista1)

##------------------------------------------------------------MODIFICAR LISTAS

print("-------------------------------------------------MODIFICAR LISTAS")
print("1) Ordenar listas con .sort() sin guardarla")
lista_numeros = [3, 10, 2, 8, 99, 101]
lista_numeros.sort() #modifica la lista, pero no la devuelve, es decir, no la guarda
print(lista_numeros)

print("2) Crear una nueva lista ordenada guardando la lista en una variable con sorted()")
lista_numeros = [3, 10, 2, 8, 99, 101]
numeros_ordenados = sorted(lista_numeros)
print(lista_numeros)
print(numeros_ordenados) #Devuelve la lista en una variable guardada

print("3) Crear una nueva lista tipo texto ordenada guardándola en una variable con sorted()")
lista_frutas = ["manzana", "pera", "limón", "manzana", "pera", "limón"]
frutas_ordenadas = sorted(lista_frutas)
print(frutas_ordenadas) #las listas tipo texto las ordena por órden alfabético de la primera letra

lista_frutas2 = ["Manzana", "Pera", "limón", "manzana", "pera", "limón"]
frutas_ordenadas2 = sorted(lista_frutas2)
print(frutas_ordenadas2) #Como criterio de orden, primero tiene en cuenta las mayúsculas

lista_frutas2.sort(key=str.lower) #De esta manera, ignora las minúsculas
print(lista_frutas2)

##------------------------------------------------------------CONTAR Y BUSCAR ELEMENTOS EN LISTAS
print("---------------------------------------CONTAR Y BUSCAR ELEMENTOS EN LISTAS")
print("emplear count.() para contar el número de veces que aparece un elemento en la lista")
print(lista_frutas2.count("manzana")) #Cuenta el número de veces está el elemento en la lista

print("manzana" in lista_frutas2) #Comprueba si el elemento existe en la lista

##--------------------------MODIFICACIÓN DE ELEMENTOS EN LISTAS EMPLEANDO BUCLES 
print("-------------MODIFICACIÓN DE ELEMENTOS EN LISTAS EMPLEANDO BUCLES")
print("1) Emplear un bucle for para convertir en mayúsculas todos los elementos en una lista de tipo texto")
animales = ["perro", "gato", "cebra", "loro", "danta", "conejo"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

#Muestra los números pares de una lista:
print("2) Emplear un bucle for y un condicional para desplegar solo los elementos pares en una lista de tipo entero")
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)


