def fatorial(num = 1, show = False):
    '''
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) mostra ou não o desenvolvimento da conta.
    :return: O valor do fatorial de um número n.
    '''
    print('--' * 20)
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c} = ' if c <= 1 else f'{c} x ', end='')
    return f'{f}'


#print(fatorial(1, True))
help(fatorial)