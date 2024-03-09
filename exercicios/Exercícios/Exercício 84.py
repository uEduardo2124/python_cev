pessoas = []
dados = []
maior = menor = 0
while True:
    print('-=' * 30)
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (Kg): ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]

    elif maior < dados[1]:
        maior = dados[1]

    elif menor > dados[1]:
        menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in pessoas:
    if maior == p[1]:
        print(f'[{p[0]}] ', end='')
print('.')
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in pessoas:
    if menor == p[1]:
        print(f'[{p[0]}] ', end='')
print('.')
