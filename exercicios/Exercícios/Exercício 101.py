def voto(a):
    from datetime import date
    atual = date.today().year
    idade = atual - a
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return f'NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'VOTO OPCIONAL'
    elif idade >= 18:
        return f'VOTO OBRIGATÓRIO'


print('--' * 20)
ano = int(input('Digite o ano que você nasceu: '))
print(voto(ano))
