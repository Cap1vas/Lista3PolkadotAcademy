def numPerfeito(num):
    i =0
    somaNumPerfeito = 0
    while True:
        i = i+1
        if(num%i==0 and i!=num):
            somaNumPerfeito = somaNumPerfeito + i
        else:
            break
    return somaNumPerfeito

entrada = int(input("numero aq"))

print(numPerfeito(entrada))
