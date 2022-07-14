#começo função volumeFeijoada
#calcula o preço base da feijoada de acordo com o volume
def volumeFeijoada():
    while True:
        try:
            volume = float(input('Entre com a quantidade de feijoada (ml):'))
            if volume < 300:
                print('Não pode ser essa quantidade. Deve ser entre 300 e 5000 ml.')
                continue
            elif 300 <= volume <= 5000:
                volume = volume * 0.08
                return volume
            elif volume > 5000:
                print('Não pode ser essa quantidade. Deve ser entre 300 e 5000 ml.')
                continue
        except ValueError:
            print('Número inválido! Tente novamente!')
            continue
#fim função volumeFeijoada

#começo função opcaoFeijoada
#escolhe o multiplicador de acordo com a opção de feijoada
def opcaoFeijoada():
    while True:
        print('*****************************************************************************************')
        print('b - Básica (Feijão + Paiol + costelinha)')
        print('p - Premium (Feijão + Paiol + costelinha + partes de porco)')
        print('s - Suprema (Feijão + Paiol + costelinha + partes do porco + charque + calabresa + bacon)')
        print('*****************************************************************************************')
        opcao = input('Escolha a opção de feijoada, conforme tabela acima:')
        opcao = opcao.upper()
        if opcao == 'B':
            return 1.00
        elif opcao == 'P':
            return 1.25
        elif opcao == 'S':
            return 1.50
        else:
            print('Opção incorreta... Tente novamente!')
            continue
#fim função opcaoFeijoada

#começo função acompanhamentoFeijoada
#retorna o preço total dos acompanhamentos
def acompanhamentoFeijoada():
    total = 0
    print('Chegou a hora dos acompanhamentos!')
    while True:
        try:
            print('0 - Não desejo mais acompanhamentos, pode encerrar o pedido')
            print('1 - 200g de arroz --------------- R$ 5,00')
            print('2 - 150g de farofa especial ----- R$ 6,00')
            print('3 - 100g de couve cozida -------- R$ 7,00')
            print('4 - 1 laranja descascada -------- R$ 3,00')
            acompanhamento = int(input('Escolha o acompanhamento desejado, conforme opções acima:'))
            if acompanhamento == 1:
                total += 5.00
                continue
            elif acompanhamento == 2:
                total += 6.00
                continue
            elif acompanhamento == 3:
                total += 7.00
                continue
            elif acompanhamento == 4:
                total += 3.00
                continue
            elif acompanhamento == 0:
                print('O programa está sendo encerrado...')
                print('Você gastou R$ {:.2f} em acompanhamentos'.format(total))
                return total
                break
            else:
                print('Você deve digitar um número inteiro entre 0 e 4!')
                continue
        except ValueError:
            print('Valor incorreto! Tente novamente!')
            continue
#fim função acompanhamentoFeijoada

#começo função main
print('**********Seja bem vindo!***********')
print('Feijoada da Maria Isabel Barudi de Matos')
valor = volumeFeijoada()
opcao = opcaoFeijoada()
print('Até agora você gastou R$ {:.2f}'.format(valor*opcao))
acompanhamento = acompanhamentoFeijoada()

total = valor * opcao + acompanhamento
print('O valor a ser pago é R$ {:.2f}'.format(total))
#fim função main