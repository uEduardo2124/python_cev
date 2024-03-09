vinte = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'douze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {vinte[num]}')
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
        if continuar == 'N':
            break
    else:
        print('Tente novamente', end=' ')
print('\033[35mEncerrado :D\033[m')
