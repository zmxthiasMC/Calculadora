import os
repetir = 'S'
while repetir == 'S'or repetir == 's':
    print("1-SUMA")
    print("2-RESTA")
    print("3-MULTIPLICACION")
    print("4-DIVISION")

    def Suma(a, b):
        return a + b

    def Resta(a, b):
        return a - b

    def Mult(a, b):
        return a * b

    def Div(a, b):
        return a/b

    choice = input("Elija una opcion:")

    valor1 = int(input("Primer numero:"))

    valor2 = int(input("Segundo numero:"))

    if choice == '1':
        resultado = Suma(valor1, valor2)
    elif choice == '2':
        resultado = Resta(valor1, valor2)
    elif choice == '3':
        resultado = Mult(valor1, valor2)
    elif choice == '4':
        resultado = Div(valor1, valor2)
    print(resultado)

    repetir = input("Desea repetir:")
    os.system('cls')

print("Fin del programa")
