preco = float(input('Digite o preço do produto: R$ '))

print('''FORMAS DE PAGAMENTO
[1] Dinheiro ou cheque
[2] Cartão à vista
[3] Cartão em 2x
[4] Cartão em 3x ou mais''')

opcao = int(input('Escolha a forma de pagamento: '))

if opcao == 1:
    total = preco - preco * 0.10
    print('Você recebeu 10% de desconto.')
    print('O valor final será R$ {:.2f}.'.format(total))

elif opcao == 2:
    total = preco - preco * 0.05
    print('Você recebeu 5% de desconto.')
    print('O valor final será R$ {:.2f}.'.format(total))

elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2 vezes sem juros.')
    print('Serão 2 parcelas de R$ {:.2f}.'.format(parcela))
    print('O valor total será R$ {:.2f}.'.format(total))

elif opcao == 4:
    parcelas = int(input('Em quantas parcelas deseja pagar? '))

    if parcelas >= 3:
        total = preco + preco * 0.20
        parcela = total / parcelas

        print('Sua compra terá 20% de juros.')
        print('Serão {} parcelas de R$ {:.2f}.'.format(parcelas, parcela))
        print('O valor total será R$ {:.2f}.'.format(total))
    else:
        print('Para essa opção, escolha 3 parcelas ou mais.')

else:
    print('Opção de pagamento inválida.')