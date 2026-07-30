from datetime import date

atual = date.today().year
menores = 0
maiores = 0

for c in range(1, 8):
    ano = int(input('Em que ano você nasceu? '))
    idade = atual - ano

    if idade < 18:
        menores += 1
    else:
        maiores += 1

print('Ao todo, {} pessoas ainda não são maiores de idade.'.format(menores))
print('Ao todo, {} pessoas já são maiores de idade.'.format(maiores))