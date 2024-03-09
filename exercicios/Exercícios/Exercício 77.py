'''palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for letra in range(0, len(palavra)):
    print(' ')
    print(f'Na palavra {palavra[letra]} temos: ', end=' ')
    for c in palavra[letra]:
        if c == 'A':
            print('a ', end='')
        elif c == 'E':
            print('e ', end='')
        elif c == 'I':
            print('i ', end='')
        elif c == 'O':
            print('o ', end='')
        elif c == 'U':
            print('u ', end='')
'''

#Resolução Guanabara
palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
           'estudar', 'praticas', 'trabalhar', 'mercado', 'programador', 'futuro')
for letra in palavra:
    print(f'\nNa palavra {letra.upper()} temos ', end='')
    for p in letra:
        if p.lower() in 'aeiou':
            print(p, end=' ')
