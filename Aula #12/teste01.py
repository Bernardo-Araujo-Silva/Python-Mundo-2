nome = str(input('Qual o seu nome? ')).strip()

if nome == 'Julia':
    print('Que nome bonito você tem!')
elif nome == 'Pedro' or nome == 'João' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é comun.')

print('Tenha um bom dia {}!'.format(nome))

#pode ser utilizado quantos elif você quiser e o else é opcional, porem é impossivel usar elif sem um if.