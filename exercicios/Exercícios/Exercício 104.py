def leiaint(frase):
    valor = 0
    ok = False
    while True:
        num = str(input(f'{frase}'))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
