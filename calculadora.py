while True:
    print("\n-Calculadora Interactiva-")
    print("Elige una operación")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Salir")
    
    opcion = input("Ingresa una opción del (1-5):")
    if opcion == "5":
        print("¡Gracias por usar nuestra calculadora! ¡Adios!")
        break
    elif opcion in ("1","2","3","4"):
        num1 = float(input("ingrese el primer número"))
        num2 = float(input("ingrese el segundo número"))
    if opcion == "1":
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == "4":
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")