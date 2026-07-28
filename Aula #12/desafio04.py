from datetime import date

nasc = int(input('Em que ano vcê nasceu? '))
atual = date.today().year
idade = atual - nasc

print('Você tem {} anos de idade.'.format(idade))

if idade < 18:
    print('Você ainda não precisa de alistar, faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Você precisa se alistar.')
elif idade > 18:
    print('Já era pra você ter se alistado! Já se passaram {} anos'.format(idade - 18))
