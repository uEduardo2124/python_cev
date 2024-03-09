n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if m >= 7:
    print('O aluno está \033[32mAPROVADO!\033[m')
elif m >= 5 and m < 7:
    print('O aluno está \033[33mEM RECUPERAÇÃO!\033[m')
else:
    print('O aluno está \033[31mREPROVADO!\033[m')
