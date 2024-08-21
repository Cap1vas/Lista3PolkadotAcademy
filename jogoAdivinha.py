import random

chuteUsuario = int(input("Digite um numero de 1 a 100"))
escolhaMaquina = random.randint(1,100)
if(chuteUsuario == escolhaMaquina):
    print("Voce acertou, parabens!")
else:
    print(f"Voce errou, a maquina escolheu o numero {escolhaMaquina}")
