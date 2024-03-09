valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S|N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=-' * 20)
valores.sort()
print(f'Você digitou os valores {valores}')
