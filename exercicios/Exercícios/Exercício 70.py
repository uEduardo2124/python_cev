total = mais1000 = baratop = baraton = 0
print('--' * 20)
print('{: ^40}'.format(' SUPER BARATÃO '))
while True:
    print('--' * 20)
    nome = str(input('Nome do produto: '))
    custo = float(input('Preço: R$'))
    if total == 0 or baratop > custo:
        baratop = custo
        baraton = nome
    total += custo
    if custo > 1000:
        mais1000 += 1
    print('--' * 20)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$\033[32m{total:.2f}\033[m.')
print(f'Temos \033[31m{mais1000}\033[m produto(s) custando mais de R$1000.00.')
print(f'O produto mais barato foi \033[35m{baraton}\033[m que custa R$\033[32m{baratop:.2f}\033[m')
