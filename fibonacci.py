def fibonacci(n):
    a, b = 0, 1
    resultado = []
    for i in range(n):
        resultado.append(a)
        a, b = b, a + b
    return resultado


entrada = int(input("Até qual termo quer ver fibonacci? "))
print(fibonacci(entrada)) 