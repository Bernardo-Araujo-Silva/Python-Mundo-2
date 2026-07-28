from time import sleep

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Você irá pagar por quantos anos? '))

parcela = casa / (anos * 12)

print('Para você comprar a casa saindo no valor de R$ {:.2f}, pagando em {} anos e tendo um salário de R$ {:.2f}, precisamos analisar a possibilidade de empréstimo.'.format(casa, anos, salario))

print('Analisando empréstimo...')
sleep(3)

if parcela > 0.30 * salario:
    print('Empréstimo negado, o valor da parcela excede 30% do seu salário.')
else:
    print('Empréstimo aprovado, você irá pagar R$ {:.2f} por mês durante {} anos.'.format(parcela, anos))