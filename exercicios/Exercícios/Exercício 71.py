'''print('==' * 20)
print('{:^40}'.format('BANCO CEV'))
print('==' * 20)
div = multi = sub = 0
cont = 1
valor = int(input('Digite o valor que deseja sacar: R$'))
while True:
    if cont == 1:
        div = valor // 50
        multi = div * 50
        sub = valor - multi
        valor = sub
        cont += 1
        print(f'Total de {div} notas de R$50' if div != 0 else '')
    elif cont == 2:
        div = valor // 20
        multi = div * 20
        sub = valor - multi
        valor = sub
        cont += 1
        print(f'Total de {div} notas de R$20' if div != 0 else '')
    elif cont == 3:
        div = valor // 10
        multi = div * 10
        sub = valor - multi
        valor = sub
        cont += 1
        print(f'Total de {div} notas de R$10' if div != 0 else '')
    elif cont == 4:
        div = valor // 1
        multi = div * 1
        sub = valor - multi
        valor = sub
        cont += 1
        print(f'Total de {div} notas de R$1' if div != 0 else '')
        break
print('==' * 20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')'''

#Resolução Guanabara
print('==' * 20)
print('{:^40}'.format('BANCO CEV'))
print('==' * 20)
valor = int(input('Digite o valor que deseja sacar: R$'))
mont = valor
ced = 50
totced = 0
while True:
    if mont >= ced:
        mont -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif ced == 1:
            ced = 0
        totced = 0
        if mont == 0:
            break