from datetime import date
ano = int(input('Digite o ano que gostaria de analisar, digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[32m{}\033[m é bissexto!'.format(ano))
else:
    print('O ano \033[31m{}\033[m NÃO é bissexto!'.format(ano))
