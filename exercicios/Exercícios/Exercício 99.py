from time import sleep
def valores(* valor):
    print('-=' * 30)
    maior = 0
    print('Analisando os valores passados...')
    print(f'Os valores informados foram: ', end='')
    for v in valor:
        print(f'{v} ', end='')
        sleep(0.4)
    print()
    print(f'Foram informados {len(valor)} valores ao todo.')
    
    for cont in range (0, len(valor)):
        if cont == 0:
            maior = valor[cont]
        else:
            if valor[cont] > maior:
                maior = valor[cont]
    print(f'O maior valor informado foi {maior}.')


valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores()
