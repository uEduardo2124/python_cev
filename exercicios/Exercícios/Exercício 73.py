tabela = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo',
          'Atlético-MG', 'Fluminese', 'São Paulo', 'Internacional',
          'Bragantino', 'Fortaleza', 'Atlético-PR', 'Cruzeiro',
          'Santos', 'Bahia', 'Corinthians', 'Cuiabá',
          'Goiás', 'América-MG', 'Vasco', 'Coritiba')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {tabela}')
print('-=' * 20)
print(f'Os primeiros 5 colocados são: {tabela[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos (lanternas): {tabela[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 20)
print(f'O Flamengo está na {tabela.index("Flamengo") + 1}.a posição')
