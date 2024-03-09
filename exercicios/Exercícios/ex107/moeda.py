def metade(num):
    res = num / 2
    return res


def dobro(num):
    res = num * 2
    return res


def aumento(num, porcentagem = 1):
    res = num + ((num * porcentagem) / 100)
    return res


def reduzir(num, porcentagem = 1):
    res = num - ((num * porcentagem) / 100)
    return res


def formatar(num):
    res = f'R${num:.2f}'
    return res


