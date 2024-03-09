from random import randint
from time import sleep
'''jogos = []
sorteio = []
print('--' * 20)
print('         JOGA NA MEGA SENA           ')
print('--' * 20)
quant = int(input('Digite quantos jogos quer sortear: '))
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for cont in range(1, (quant) + 1):
    for c in range(0, 6):
        num = randint(1, 60)
        for n in range(0, len(sorteio)):
            if num == sorteio[n]:
                num = randint(1, 60)
        sorteio.append(num)
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()

for p in range(0, len(jogos)):
    print(f'Jogo {p + 1}: {jogos[p]}')
    sleep(1)
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)'''

#Resolução Guanabara
lista = []
jogos = []
tot = 1
print('--' * 30)
print('     JOGA NA MEGA SENA       ')
print('--' * 30)
quant = int(input('Digite quantos jogos quer sortear: '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')
    sleep(1)
print('-=' * 5, ' < BOA SORTE > ', '-=' * 5)
