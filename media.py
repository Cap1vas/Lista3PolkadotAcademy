i = 0
total = 0

while True:
    nota = int(input("Digite a nota de um aluno (-1 para sair)"))
    if nota == -1:
        break
    i += 1
    total += nota
    print("A média das notas é:", total / i)