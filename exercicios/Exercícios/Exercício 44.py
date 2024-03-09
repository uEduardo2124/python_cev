print('{:=^40}'.format(' LOJAS SLA '))
v = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO: )
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
c = int(input('Qual irá escolher: '))
if c == 1:
    f = (v - (v * 10) / 100)
elif c == 2:
    f = (v - (v * 5) / 100)
elif c == 3:
    f = (v + (v * 20) / 100)
    t = (f / 2)
    print('Sua compra será parcelada em 2x de \033[32mR${:.2f}\033[m COM JUROS'.format(t))
elif c == 4:
    p = int(input('Digite o número de parcelas que deseja: '))
    f = (v + (v * 20) / 100)
    t = (f / p)
    print('Sua compra será parcelada em {}x de R$\033[32m{:.2f}\033[m COM JUROS'.format(p, t))
else:
    print('Opção inválida, tente novamente!')
print('Sua compra de R$\033[31m{:.2f}\033[m vai custar R$\033[32m{:.2f}\033[m no final'.format(v, v))
