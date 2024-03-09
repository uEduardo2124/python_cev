lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort(reverse = True)

print('-=' * 30)
print(f'Você digitou um total de {len(lista)} elementos.')
print(f'Os valores em ordem descrescente são {lista}')

print('O valor 5 \033[32mfaz parte\033[m da lista' if 5 in lista else 'O valor 5 \033[31mNÂO\033[m foi encontrado na lista')
