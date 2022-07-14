#funcao mensagem_valor(), imprime mensagem e valor maior
#desisto
def mensagem_valor(mensagem, numeros):
   print(mensagem)
   total = 0
   j = 0
   maior = 0
   for j in numeros:
        total += 1
   for i in range(total):
        if numeros[i] == maior:
            continue
        elif numeros[i] > maior:
            maior = numeros[i]
            continue
        elif numeros[i] < maior:
            continue
   return maior



frase = input('Escreva uma mensagem pra todos!\n')
tupla_numeros = (52,23,19,74,64,91,45,87,38,79)
mensagem_2 = mensagem_valor(frase, tupla_numeros)
print(mensagem_2)
