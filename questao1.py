# usuário entra com valor e quantidade de um certo produto e recebe o valor a
# pagar e desconto concedido, se for o caso

print('************** Seja bem vindo! **************')
print('*** Bazar da Maria Isabel Barudi de Matos ***')

# criação de variáveis para receber os dados do usuário
valor3996720 = float(input('Qual é o valor do produto?\n'))
quantidade = int(input('Qual é a quantidade que você precisa?\n'))

# quantidade de produtos é menor ou igual 4
if quantidade <= 4 and quantidade > 0:
    print('Valor a pagar: R${}'.format(quantidade*valor3996720))
    print('Até 4 unidades não temos desconto!')
# quantidade de produtos está entre 5 e 19
elif quantidade >= 5 and quantidade <= 19:
    print('Valor a pagar sem desconto: R$ {}'.format(quantidade*valor3996720))
    print('Desconto de 3%.')
    print('Valor a pagar com desconto: R$ {}'.format(quantidade*valor3996720 - quantidade*valor3996720*0.03))
# quantidade de produtos está entre 20 e 99
elif quantidade >=20 and quantidade <= 99:
    print('Valor a pagar sem desconto: R$ {}'.format(quantidade * valor3996720))
    print('Valor a pagar com desconto: R$ {}'.format(quantidade * valor3996720 - quantidade * valor3996720 * 0.06))
    print('Desconto de 6%.')
# quantidade de produtos é maior ou igual a 100
elif quantidade >= 100:
    print('Valor a pagar sem desconto: R$ {}'.format(quantidade * valor3996720))
    print('Valor a pagar com desconto: R$ {}'.format(quantidade * valor3996720 - quantidade * valor3996720 * 0.1))
    print('Desconto de 10%')
# entrada de número menor ou igual a 0
else:
    print('Quantidade inválida!')