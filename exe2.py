# media dos pares de 1 ate 100
soma = 0
quantidade = 0
for i in range(1, 101, 1):
    if i % 2 == 0:
        soma += i
        quantidade += 1
media = soma / quantidade
print(media)
