sen = 'O Banco do Brasil faz muitas festas!'
i = 0
maior = ' '
palavras = sen.split()
quant_palavras = len(palavras)
for i in range(quant_palavras):
    tamanho = len(palavras[i])
    if tamanho > len(maior):
        maior = palavras[i]
print(maior)