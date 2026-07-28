from datetime import date

print('=' * 30)
print('CATEGORIAS POR IDADE')
print('=' * 30)

ano = int(input('Em que ano o atleta nasceu? '))
atual = date.today().year
idade = atual - ano

print('Você tem {} anos'.format(idade))

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JÚNIOR')
elif idade <= 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')