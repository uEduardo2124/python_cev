def metade(num = 0, formato = False, money = 'R$'):
    '''
    -> Função para determinar a metade de um valor
    :param num: valor a ser recebido para verificar sua metade
    :param formato: variável booleana para caso queira formatar os valores como um valor em moeda
    :param money: moeda desejada (ex.: real, dólar, euro, yene e etc..)
    :return: retorna a metade do valor
    '''
    res = num / 2
    return res if formato is False else formatar(res)

def dobro(num = 0, formato = False, money = 'R$'):
    res = num * 2
    return res if formato is False else formatar(res)


def aumento(num = 0, porcentagem = 0, formato = False, money = 'R$'):
    res = num + ((num * porcentagem) / 100)
    return res if formato is False else formatar(res)


def reduzir(num = 0, porcentagem = 0, formato = False, money = 'R$'):
    res = num - ((num * porcentagem) / 100)
    return res if formato is False else formatar(res)


def formatar(num = 0, money = 'R$'):
    res = f'{money}{num:>.2f}'.replace('.', ',')
    return res


