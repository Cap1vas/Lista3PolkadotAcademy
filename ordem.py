
print("Olá! Por favor, digite três números diferentes:")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))


if num1 == num2 or num1 == num3 or num2 == num3:
    print("Oops! Os números devem ser diferentes. Tente novamente!")
else:

    numeros = [num1, num2, num3]
    numeros.sort()
    print("Os números em ordem crescente são:", numeros[0], numeros[1], numeros[2])