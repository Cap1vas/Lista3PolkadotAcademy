numeros = []

while True:
    num = input("Insira um número (ou 'sair' para finalizar): ")
    if num.lower() == 'sair':
        break
    try:
        num = float(num)
        numeros.append(num)
    except ValueError:
        print("Erro: Insira um número válido!")

if len(numeros) == 0:
    print("Nenhum número foi inserido!")
else:
    maior = max(numeros)
    menor = min(numeros)
    media = sum(numeros) / len(numeros)

    print(f"Maior número: {maior:.2f}")
    print(f"Menor número: {menor:.2f}")
    print(f"Média dos números: {media:.2f}")