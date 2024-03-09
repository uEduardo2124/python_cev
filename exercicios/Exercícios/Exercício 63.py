print('--' * 20)
print('SEQUÊNCIA DE FIBONACCI')
print('--' * 20)
n = int(input('Digite quantos termos deseja mostrar: '))
c = 3
t1 = 0
t2 = 1
t3 = 0
print('~~' * 20)
print('{} -> {} -> '.format(t1, t2), end='')
while c <= n:
    t3 = (t1 + t2)
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('FIM!')
print('~~' * 20)
