soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

    if sexo == 'F':
        if idade < 20:
            mulheres_menos_20 += 1

media = soma_idade / 4

print('A média de idade do grupo é {:.2f} anos.'.format(media))

if nome_homem_mais_velho == '':
    print('Nenhum homem foi cadastrado.')
else:
    print('O homem mais velho se chama {} e tem {} anos.'.format(
        nome_homem_mais_velho, maior_idade_homem
    ))

print('{} mulher(es) têm menos de 20 anos.'.format(mulheres_menos_20))