jogador = {}
geral = []
gol = []
while True:
    jogador.clear()
    gol.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for p in range (0, partidas):
        gol.append(int(input(f'      Quantidade de gols na partida {p + 1}: ')))

    jogador['gol'] = gol[:]
    jogador['total'] = sum(gol)
    geral.append(jogador.copy())

    while True:
        continuar = str(input('Deseja continuar [S|N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO!, Por favor, digite apenas Sim(S) ou Não(N).')
    if continuar == 'N':
        break

print('-=' * 30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(geral):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    resposta = int(input('Mostrar dados de qual jogador (999 para parar): '))

    if resposta == 999:
        break
    elif resposta >= len(geral):
        print(f'ERRO! Não existe jogador com código {resposta}')
    else:
            print(f' -- LEVANTAMENTO DO JOGADOR {geral[resposta]["nome"]}: ')
            for n, g in enumerate(geral[resposta]['gol']):
                print(f'       No jogo {n + 1}, fez {g} gols')
    print('-' * 40)
print(' << VOLTE SEMPRE >>')
