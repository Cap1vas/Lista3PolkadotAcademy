def verificaPalindromo(palavra):
    invertida = palavra[::-1]
    if(palavra == invertida):
        return True
    else:
        return False

palavra = str(input("Digite uma palavra")).strip()

print(verificaPalindromo(palavra))


