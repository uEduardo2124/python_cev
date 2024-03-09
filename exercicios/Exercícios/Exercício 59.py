from time import sleep
n1 = (int(input('Primeiro valor: ')))
n2 = (int(input('Segundo valor: ')))
c = False
maior = 0
while not c:                                            # ou "o != 5"
    o = int(input('''    [ 1 ] \033[31mSomar\033[m
    [ 2 ] \033[32mMultiplicar\033[m
    [ 3 ] \033[33mMaior\033[m
    [ 4 ] \033[34mNovos números\033[m
    [ 5 ] \033[35mSair do Programa\033[m
>>>>>> Digite sua opção: '''))
    if o == 1:
        print('Soma: {} + {} = \033[32m{}\033[m'.format(n1, n2, n1 + n2))
        print('=-=' * 10)
    elif o == 2:
        print('Multiplicação: {} x {} = \033[32m{}\033[m'.format(n1, n2, (n1 * n2)))
        print('=-=' * 10)
    elif o == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é \033[32m{}\033[m'.format(n1, n2, maior))
        print('=-=' * 10)
    elif o == 4:
        print('\033[34mInforme os números novamente: \033[m')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif o == 5:
        c = True
        print('\033[32mFinalizando...\033[m')
        print('=-=' * 10)
        sleep(1)
        print('\033[32mFim do programa! Volte sempre!\033[m')
    else:
        print('\033[31mOpção inválida. Tente novamente!\033[m')
        print('=-=' * 10)
