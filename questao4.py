#----------- começo cadastrarProduto()-----------
def cadastrarProduto(codigo):
        while True:
            try:
                nome = input('Digite o nome do produto:\n')
                fabricante = input('Digite o fabricante do produto:\n')
                valor = float(input('Digite o valor do produto:\n'))
                dicionarioProduto = {'codigo': codigo, 'nome': nome,'fabricante': fabricante, 'valor': valor}
                lista.append(dicionarioProduto.copy())
                continua = input('Vocë quer cadastrar novo produto? (s/n)')
                print('----------------------------------------')
                if continua.lower() == 's':
                    codigo +=1
                    continue
                elif continua.lower() == 'n':
                    return codigo
                else:
                    print('Digite um valor válido!')
                    break
            except ValueError:
                print('Digite um valor válido!')
#---------------fim cadastrarProduto()-----------

#----------- começo consultarProduto()-----------
def consultarProduto():
    while True:
        try:
            print('----------------------------------')
            opcao1 = int(input('Escolha a opção desejada:\n1 - Consultar todos os produtos\n2 - Consultar produtos por código\n'
            '3 - Consultar produtos por fabricante\n4 - Retornar\n'))
            if opcao1 == 1:
                for item in lista:
                    print('----------------------------------')
                    for key,value in item.items():
                        print("{} : {}".format(key, value))
            elif opcao1 == 2:
                cod = int(input('Qual é o código do produto que você quer pesquisar?'))
                for item in lista:
                    print('----------------------------------')
                    if item['codigo'] == cod:
                        for key, value in item.items():
                            print("{} : {}".format(key,value))
            elif opcao1 == 3:
                fab = (input('Qual é o fabricante que você quer pesquisar?'))
                for item in lista:
                    print('----------------------------------')
                    if item['fabricante'] == fab:
                        for key, value in item.items():
                            print("{} : {}".format(key,value))
            elif opcao1 == 4:
                break
            else:
                print('Digite um valor válido!')
                continue
        except ValueError:
            print('Digite um valor válido!')


#---------------fim consultarProduto()-----------

#------------- começo removerProduto()-----------
def removerProduto():
    cod = int(input('Qual é o código do produto que você quer remover?'))
    for item in lista:
        if item['codigo'] == cod:
            lista.remove(item)
#-----------------fim removerProduto()-----------

#------------------------- começo main-----------
print('Mercearia da Maria Isabel Barudi de Matos')
codigo = 0
lista = []
while True:
    try:
        opcao = int(input('Escolha a opção desejada:\n1 - Cadastrar produto\n2 - Consultar produto\n3 - Remover produto(s)\n'
            '4 - Sair\n'))
        if opcao == 1:
            codigo +=1
            print('Bem-vindo ao cadastro de produtos!')
            print('----------------------------------')
            codigo = cadastrarProduto(codigo)
            continue
        elif opcao == 2:
            print('Bem-vindo à consulta de produtos! ')
            print('----------------------------------')
            consultarProduto()
            continue
        elif opcao == 3:
            print('Benm-vindo à remoção de produtos!')
            print('----------------------------------')
            removerProduto()
            continue
        elif opcao == 4:
            print('Programa sendo encerrado...')
            break
        else:
            print('Digite um valor válido!')
            continue
    except ValueError:
        print('Digite um valor válido!')
#-----------------------------fim main-----------
