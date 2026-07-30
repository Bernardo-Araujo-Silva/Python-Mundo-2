n = int(input('Digite um núero que queira saber a tabuada: '))

print('A tabuada do número {} é...'.format(n))

for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n * c))