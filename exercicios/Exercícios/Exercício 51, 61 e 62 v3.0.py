#Versão for
'''print('==' * 20)
print(' TERMOS DE UMA PA    ')
print('==' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print('{} '.format(c), end=' -> ')
print('ACABOU')'''

#Versão while v3.0
print('-=' * 20)
print(' TERMOS DE UMA PA    ')
print('-=' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = p
c = 1
ct = 1
s = 10
tot = 0
while s != 0:
    tot = tot + s
    while c <= tot:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    print('PAUSA!')
    s = int(input('Quantos termos deseja mostrar a mais: '))
print('Progressão finalizada com {} termos mostrados!'.format(tot))
