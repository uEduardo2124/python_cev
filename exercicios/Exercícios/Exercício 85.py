valores = [[], []]
valor = 0
for cont in range(0, 7):
    valor = int(input(f'Digite o {cont + 1}.o valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print('-=' * 30)
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
