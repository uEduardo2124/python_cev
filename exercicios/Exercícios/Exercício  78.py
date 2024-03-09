valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    elif maior < valores[cont]:
        maior = valores[cont]
    elif menor > valores[cont]:
        menor  = valores[cont]

print('=-' * 30)
print(f'Você digitou os valores {valores}', end='')

print(f'\nO maior valor digitado foi|foram {maior} na(s) posição(ões) ', end='')
for p in range(0, len(valores)):
    if maior == valores[p]:
        print(f'{p}... ', end='')
print('')

print(f'O menor valor digitado foi|foram {menor} na(s) posição(ões) ', end='')
for p in range(0, len(valores)):
    if menor == valores[p]:
        print(f'{p}... ', end='')
print('')
