entrada = int(input("Insira o fatorial que deseja calcular"))

fatorial = 1
for i in range(1,entrada+1):
    fatorial = (fatorial * i)
    print(fatorial)