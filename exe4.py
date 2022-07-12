ano_atual = int(input('Qual eh o ano atual?\n'))
ano_nascimento = int(input('Qual o ano que voce nasceu?\n'))
idade = ano_atual - ano_nascimento
print(idade)
if idade >= 18:
    print('Voce jah pede tirar carteira de motorista!')
else:
    print('Voce eh menor de idade, naun pode tirar carteira de motorista ainda!')