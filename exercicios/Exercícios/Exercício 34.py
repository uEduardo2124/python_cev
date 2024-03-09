s = float(input('Digite o salário do funcionário: R$'))
if s > 1250:
    a = s + ((s * 10) / 100)
else:
    a = s + ((s * 15) / 100)
print('O funcionário que ganhava R$\033[31m{:.2f}\033[m passa a ganhar R$\033[32m{:.2f}\033[m'.format(s, a))
