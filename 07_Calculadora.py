##---------CALCULADORA PYTHON
# 1) Función de suma:
def Suma(x, y):
    return x + y

# 2) Función de resta:
def Sustraccion(x, y):
    return x - y

# 3) Función de multiplicación:
def Multiplicacion(x, y):
    return x * y

# 4) Función de división:
def Division(x, y):
    return x / y

# 5) Función de módulo:
def Modulo(x, y):
    return x % y

print("Select operation.")
print("1.Suma")
print("2.Sustraccion")
print("3.Multiplicacion")
print("4.Division")
print("5.Modulo")

while True:
    # Tomar el input del usuario:
    choice = input("Escoge una opción(1/2/3/4/5): ")

    # Revisar las opciones:
    if choice in ("1", "2", "3", "4", "5"):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if choice == "1":
            print(num1, "+", num2, "=", Suma(num1, num2))

        elif choice == "2":
            print(num1, "-", num2, "=", Sustraccion(num1, num2))

        elif choice == "3":
            print(num1, "*", num2, "=", Multiplicacion(num1, num2))

        elif choice == "4":
            print(num1, "/", num2, "=", Division(num1, num2))

        elif choice == "5":
            print(num1, "%", num2, "=", Modulo(num1, num2))

        # Revisa si el usuario quiere realizar otro cálculo:
        next_calculation = input("¿Quieres ejecutar otro cálculo?(Si/No): ")
        if next_calculation == "No":
            break

        else:
            print("OK, continuemos")
