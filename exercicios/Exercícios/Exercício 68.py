from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = (jogador + computador)
    tipo = str(input('Par ou Ímpar [P|I]: ')).strip().upper()[0]
    print('--' * 20)
    print(f'Você jogou {jogador} e a máquina jogou {computador}. Total de {total}', end=' ')
    final = ''
    if total % 2 == 0:
        print('DEU PAR')
        final = 'P'
    else:
        print('DEU ÍMPAR')
        final ='I'
    print('--' * 20)
    if tipo == final:
        print('Você VENCEU!\nVamos jogar novamente...')
        cont += 1
        print('=-' * 20)
    else:
        print('Você PERDEU!')
        print('=-' * 20)
        break
print(f'GAME OVER! Você venceu {cont} vezes')
