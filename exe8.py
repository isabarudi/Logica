acumulador=0 # muito importante inicializar o acumulador com zero
print('Seja bem vindo ao salão da Maria Isabel Barudi de Matos')
print('********Opções de serviços:********')
print('| Código | Descrição          | Valor    |')
print('| cc     | Corte de Cabelo    |  80,00   |')
print('| pe     | Penteado Elaborado | 220,00   |')
print('| pi     | Pintura            | 120,00   |')
print('| pr     | Progressiva        | 450,00   |')
print('| es     | Escova             | 100,00   |')
while True:
    codigo = input('Entre com o código do serviço desejado:')
    if codigo =='cc':
        acumulador = acumulador + 80
    elif codigo == 'pe':
        acumulador = acumulador + 220
    elif codigo == 'pi':
        acumulador = acumulador + 120
    elif codigo == 'pr':
        acumulador = acumulador + 450
    elif codigo == 'es':
        acumulador = acumulador + 100
    else:
        print('Pare de digitar caracteres errados')
        continue
    print('O valor até agora é: {:.2f}'.format(acumulador))
    resposta = input('Desseja mais algum serviço? s/n')
    if resposta == 's':
        continue
    else:
        print('O valor final da conta é: {:.2f}'. format(acumulador))
        break
