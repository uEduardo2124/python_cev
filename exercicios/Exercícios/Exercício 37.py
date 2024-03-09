n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão')
'[ 1 ] converter para BINÁRIO
'[ 2 ] converter para OCTAL
'[ 3 ] converter para HEXADECIMAL''')
c = int(input('Sua opção: '))
if c == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif c == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif c == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente!')