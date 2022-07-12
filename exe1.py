inicial = int(input('Você deseja iniciar a contagem com qual valor?\n'))
final = int(input('Você deseja encerrar a contagem com qual valor?\n'))
x = inicial
while x <= final:
    if x % 2 == 0:
        print(x)
    x = x + 1
