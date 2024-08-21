entrada = str(input("Digite uma palavra"))

vogais = 'aeiou'
contador_vogais = 0

for caractere in entrada:
    if caractere.lower() in vogais:
        contador_vogais += 1

print(f"A palavra contém {contador_vogais} vogais")