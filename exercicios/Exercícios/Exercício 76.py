tabela = ('Lápis', 1.75,
          'Borracha', 2,
          'Caderno', 15.90,
          'Estojo', 25,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.30,
          'Livro', 34.90)
print('--' * 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--' * 20)
for c in range(0, len(tabela)):
    if c % 2 == 0:
        print(f'{tabela[c]:.<30}', end='')
    else:
        print(f'R${tabela[c]:>7.2f}')
print('--' * 20)
