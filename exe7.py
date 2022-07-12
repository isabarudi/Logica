sen = 'Cats AND*Dogs-are Awesome'
frase = [ ]
frase1 = [ ]
frase2 = [ ]

palavras = sen.split()
for i in range(len(palavras)):
    outras_palavras = palavras[i].split('*')
    frase = frase + outras_palavras
for i in range(len(frase)):
    novas_palavras = frase[i].split('-')
    frase1 = frase1 + novas_palavras
for i in range(len(frase1)-1):
    if i == 0:
        frase2 = frase1[i].lower()
    else:
        frase2 = frase2 + frase[i].title()
print(frase2)
