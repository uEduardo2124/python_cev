s = float(input('Digite o salário atual do funcionário: R$'))
aumento = s + ((s * 15)/ 100)
print('O funcionário que ganhava R${:.2f}, com o aumento de 15%, passa a receber R${:.2f}'.format(s, aumento))