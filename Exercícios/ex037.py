numero = int(input('Digite um número inteiro: '))

print('''ESCOLHA UMA BASE PARA CONVERSÃO:
[1] Binário
[2] Octal
[3] Hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(
        numero, bin(numero)[2:]
    ))

elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(
        numero, oct(numero)[2:]
    ))

elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(
        numero, hex(numero)[2:]
    ))

else:
    print('Opção inválida! Escolha 1, 2 ou 3.')