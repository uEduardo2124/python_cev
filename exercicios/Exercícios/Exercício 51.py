print('==' * 20)
print(':^510 TERMOS DE UMA PA')
print('==' * 20)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print('{} '.format(c), end=' -> ')
print('ACABOU')
