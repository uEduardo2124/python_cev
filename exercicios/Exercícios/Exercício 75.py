numero = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
tres = 0
print(f'Você digitou os valores: {numero}')
print(f'O valor 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O valor 3 apareceu na {numero.index(3) + 1}.a posição')
else:
    print(f'O valor 3 não apareceu nenhuma vez')
print('O(s) valor(es) par(es) digitado(s) foi|foram: ', end='')
for c in numero:
    if c % 2 == 0:
        print(f'{c}', end=' ')
