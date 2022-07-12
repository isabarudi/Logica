print('Pizzaria da Maria Isabel Barudi de Matos')
print('******************** Cardápio *********************')
print('| Código | Descrição  | Pizza Média | Pizza Grande |')
print('| 21     | Napolitana | R$20,00     | R$ 26,00     |')
print('| 22     | Margherita | R$20,00     | R$ 26,00     |')
print('| 23     | Calabresa  | R$25,00     | R$ 32,00     |')
print('| 24     | Toscana    | R$30,00     | R$ 39,00     |')
print('| 25     | Portuguesa | R$30,00     | R$ 39,00     |')
total = 0   # variável que acumula valor a ser pago pelo cliente
while True:
    tamanho = input('Qual tamanho de pizza deseja? (M/G)')   # recebe o tamanho da pizza escolhido
    tamanho = tamanho.upper()   # converte a opção do cliente em letra maiúscula
    if tamanho != 'M' and tamanho != 'G':
        print('Opção Inválida')  # mensagem de erro caso o cliente escolha um tamanho que não existe
        continue
    cod_sabor = input('Entre com o código do sabor desejado:')   # recebe o sabor da pizza escolhido
    # de acordo com o tamanho e sabor escolhidos, a  variável total é acumulada
    if cod_sabor == '21':
        sabor = 'Napolitana'
        if tamanho == 'M':
            total += 20
        else:
            total += 26
    elif cod_sabor == '22':
        sabor = 'Margherita'
        if tamanho == 'M':
            total += 20
        else:
            total += 26
    elif cod_sabor == '23':
        sabor = 'Calabresa'
        if tamanho == 'M':
            total += 25
        else:
            total += 32
    elif cod_sabor == '24':
        sabor = 'Toscana'
        if tamanho == 'M':
            total += 30
        else:
            total += 39
    elif cod_sabor == '25':
        sabor = 'Portuguesa'
        if tamanho == 'M':
            total += 30
        else:
            total += 39
    else:
        print('Sabor incorreto')   # mensagem de erro caso o cliente escolha o código incorreto
        continue
    print('Você pediu uma pizza {} tamanho {}. Total até agora R${:.2f}'.format(sabor, tamanho, total))
    opcao = input('Deseja pedir mais alguma coisa? (s/n)')
    opcao = opcao.upper()
    if opcao == 'S':
        continue
    else:
        print('O total a pagar é: R$ {:.2f}'.format(total))   # encerra o programa
        break