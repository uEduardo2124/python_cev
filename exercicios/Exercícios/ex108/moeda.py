def metade(num = 0):
    res = num / 2
    return res


def dobro(num = 0):
    res = num * 2
    return res


def aumento(num = 0, porcentagem = 0):
    res = num + ((num * porcentagem) / 100)
    return res


def reduzir(num = 0, porcentagem = 0):
    res = num - ((num * porcentagem) / 100)
    return res


def formatar(num = 0, money = 'R$'):
    res = f'{money}{num:>.2f}'.replace('.', ',')
    return res


