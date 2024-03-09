v = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento: '))
p = (v / (a * 12))
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(v, a, p))
if p >= ((s * 30) / 100):
    print('Empréstimo \033[31mNEGADO!\033[31m')
else:
    print('Empréstimo \033[32mAPROVADO!\033[m')