n = int(input('Digite um número: '))
contador = 0

for c in range(1, n + 1):
    if n % c == 0:
        contador += 1

if contador == 2:
    print('O número é primo.')
else:
    print('O número não é primo.')