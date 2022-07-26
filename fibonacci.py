fibo = [ ]
while True:
    try:
        numero = int(input('Entre com o número a ser verificado!\n'))
        fibo.insert(0, 0)
        fibo.insert(1, 1)
        i = 2
        soma = 0
        while soma <= numero:
            soma = fibo[i - 1] + fibo[i - 2]
            fibo.insert(i, soma)
            num = fibo[i - 1]
            i += 1
        print(fibo)
        if num == numero:
            print('O número {} pertence à sequência de Fibonacci.'.format(numero))
            break
        else:
            print('O número {} não pertence à sequência de Fibonacci.'.format(numero))
            break
    except ValueError:
        print('Entre com um número inteiro!')
