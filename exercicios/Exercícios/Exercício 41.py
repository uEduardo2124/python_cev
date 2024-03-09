from datetime import date
y = date.today().year
a = int(input('Ano de nascimento: '))
i = (y - a)
print('O atleta tem {} anos'.format(i))
print('Classificação: ', end= '')
if i <= 9:
    print('\033[31mMirim\033[m')
elif i <= 14:
    print('\033[32minfantil\033[m')
elif i <= 19:
    print('\033[33mJunior\033[m')
elif i <= 25:
    print('\033[34mSenior\033[m')
else:
    print('\033[34mMaster\033[m')
