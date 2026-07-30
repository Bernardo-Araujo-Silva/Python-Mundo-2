frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('A frase normal é: {}'.format(junto))
print('A frase ao contrário é: {}'.format(inverso))

if junto == inverso:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')