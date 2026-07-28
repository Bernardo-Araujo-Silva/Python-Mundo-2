from time import sleep

n1 = float(input('Digite sua 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
m = (n1 + n2) / 2

print('Sua média final foi {}'.format(m))
print('Calculando situação...')
sleep(3)

if m < 5.0:
    print('Infelizmente você foi reprovado, estude mais!')
elif 5.0 <= m <= 6.9:
    print('Você está de recuperação, boa sorte!')
else:
    print('Meus parabéns, você foi aprovado!')