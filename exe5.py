#cálculo de bonus conforme tempo do funci na empresa
nome = input('Qual eh o seu nome?')
salario = float(input('Qual eh seu salario?'))
tempo = float(input('Quantos anos voce tem de empresa?\n'))
if tempo > 5:
    bonus = salario * 0.2
    salario_final = salario + bonus
    print('{} tem {} anos de empresa. Receberah um bonus de R${}.\n'.format(nome, tempo, bonus))
    print('O salario total do {} serah {}.\n'.format(nome, salario_final))
else:
    bonus = salario * 0.1
    salario_final = salario + bonus
    print('{} tem {} anos de empresa. Receberah um bonus de R${}.\n'.format(nome, tempo, bonus))
    print('O salario total do {} serah {}.\n'.format(nome, salario_final))