n = int(input('Me diga um número qualquer: '))
if n % 2 == 0:
    print('O número {} é \033[32mPAR!\033[m'.format(n))
else:
    print('O número {} é \033[31mÍMPAR!\033[m'.format(n))
