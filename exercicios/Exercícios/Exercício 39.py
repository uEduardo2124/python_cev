from datetime import date
genero = str(input('Digite seu gênero: ')).strip()
if genero.upper() == 'MASCULINO':
    nasc = int(input('Digite o seu ano de nascimento: '))
    atual = date.today().year
    idade = (atual - nasc)
    print('Quem nasceu em {} tem {} ano(n2) em {}'.format(nasc, idade, atual))
    if idade > 18:
        print('Você deveria ter se alistado há {} ano(n2)'.format((idade - 18)))
        print('Seu alistamento foi em {}'.format((nasc + 18)))
    elif idade == 18:
        print('Você tem que se alistar \033[31mIMEDIATAMENTE!\033[m')
    else:
        print('Você ainda não tem 18 anos, ainda faltam {} ano(n2) para seu alistamento'.format((18 - idade)))
        print('Seu alistamento será em {}'.format(nasc + 18))
else:
    print('Você não precisa fazer o alistamento!')
