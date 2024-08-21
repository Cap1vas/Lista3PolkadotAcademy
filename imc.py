def calculaIMC (peso,altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))
print(calculaIMC(peso,altura))