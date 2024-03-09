#1 forma de fazer:
'''frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso da frase {} é {}'.format(junto, inverso))
if junto == inverso:
    print('\033[32mÉ um palíndromo\033[m!')
else:
    print('\033[31mNÂO É um palíndromo\033[m!')'''

#2 forma de fazer:
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso da frase {} é {}'.format(junto, inverso))
if junto == inverso:
    print('\033[32mÉ um palíndromo\033[m!')
else:
    print('\033[31mNÃO É um palíndromo\033[m!')
