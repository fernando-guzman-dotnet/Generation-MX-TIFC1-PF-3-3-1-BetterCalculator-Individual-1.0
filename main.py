def addmultiplenumbers(numbers):
    """
    Suma una lista de números.
    """
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    """
    Multiplica una lista de números.
    """
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    """
    Devuelve True si el número es entero y par, False en cualquier otro caso.
    """
    return isinstance(num, int) and num % 2 == 0

def isitaninteger(num):
    """
    Devuelve True si el número es entero, False en cualquier otro caso.
    """
    return isinstance(num, int)

def main():
    print("Hello learners!")
    print("Bienvenido a la Calculadora Avanzada")

    while True:
        print("\n¿Qué operación deseas realizar?")
        print("1. Sumar varios números")
        print("2. Multiplicar varios números")
        print("3. Verificar si un número es par")
        print("4. Verificar si un número es entero")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            nums = input("Ingresa los números separados por espacio: ")
            lista = [float(n) for n in nums.split()]
            print("Resultado de la suma:", addmultiplenumbers(lista))

        elif opcion == '2':
            nums = input("Ingresa los números separados por espacio: ")
            lista = [float(n) for n in nums.split()]
            print("Resultado de la multiplicación:", multiplymultiplenumbers(lista))

        elif opcion == '3':
            num = float(input("Ingresa un número: "))
            print("¿Es par?", isiteven(num))

        elif opcion == '4':
            num = float(input("Ingresa un número: "))
            print("¿Es un número entero?", isitaninteger(num))

        elif opcion == '5':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
