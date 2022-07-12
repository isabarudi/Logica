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
def opcaoFeijoada():

#fim função opcaoFeijoada
#começo função acompanhamentoFeijoada
#def acompanhamentoFeijoada():
#fim função acompanhamentoFeijoada
#começo função main
print('**********Seja bem vindo!***********')
print('Feijoada da Maria Isabel Barudi de Matos')
valor = volumeFeijoada()
print('O valor a ser pago é R$ {:.2f}'.format(valor))
#fim função main