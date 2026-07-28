a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print('Esses comprimentos de retas podem formar um triângulo!')

            if a == b and b == c:
                print('O triângulo é EQUILÁTERO.')
            elif a == b or a == c or b == c:
                print('O triângulo é ISÓSCELES.')
            else:
                print('O triângulo é ESCALENO.')

        else:
            print('Não é possível formar um triângulo com essas medidas.')
    else:
        print('Não é possível formar um triângulo com essas medidas.')
else:
    print('Não é possível formar um triângulo com essas medidas.')