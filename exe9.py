linda = ('Maria', 'Isabel', 'Eduarda', 'Rosa', 'Noemia', 'Julia', 'Meise', 'Antonia', 'Adriana', 'Fabiane')
# numerar e listar
i = 0
for j in linda:
    i += 1
    bonita = linda[i-1]
    print(i, linda[i-1])
print()

# numerar e listar os 3 primeiros
i = 0
j = ' '
for i in range(1,4):
    print('A numero {} eh {}'.format(i,linda[i - 1]))
print()

#numerar e listar os 5 ultimos
i = 0
j = ' '
for i in range(-5,0):
    print('A numero {} eh {}'.format(i + 11, linda[i + 9]))
print()
#encontrar a posicao de Eduarda na tupla
i = 0
j = ' '
for j in linda:
    i += 1
    if j == 'Eduarda':
        print('A Eduarda esta na posicao {}'.format(i))