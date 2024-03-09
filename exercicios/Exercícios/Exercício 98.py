from time import sleep
def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)
    if i < f:
        for cont in range (i, f + 1, p):
            print(f'{cont} ', end='')
            sleep(0.5)
        print('FIM!')
    else:
        for cont in range (i, f - 1, -p):
            print(f'{cont} ', end='')
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
