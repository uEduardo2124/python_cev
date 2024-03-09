def area(larg , comp):
    a = larg * comp
    print(f'A àrea de um terreno {l}x{c} é de {a} metros quadrados')


print('Controle de Terrenos')
print('--' * 10)
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
area(l ,c)
