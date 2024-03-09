jogador = {}
gol = []
totgol = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for p in range (0, partidas):
    gol.append(int(input(f'    Quantidade de gols na partida {p + 1}: ')))

jogador['gol'] = gol[:]
jogador['total'] = sum(gol)

print('-=' * 30)
print(jogador)

print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gol"])} partidas.')
for n, g in enumerate(gol):
    print(f'    => Na partida {n + 1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
