
def temp(entrada,temp):
  if(entrada == 'k'):
    temp = temp + 273.15
  else: 
    if(entrada == 'f'):
      temp = (temp * 9/5) +32

  return temp


entrada = input("Qual a unidade de temperatura?").lower()
temperatura = float(input("Qual a temp em C? "))
print(entrada)
print(temp(entrada,temperatura))
