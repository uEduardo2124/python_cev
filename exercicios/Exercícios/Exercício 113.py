def leiaint(frase):
    while True:
        try:
            valor = int(input(f'{frase}'))
        except (TypeError, ValueError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return valor


def leiareal(frase):
    while True:
        try:
            valor = float(input(f'{frase}'))
        except (TypeError, ValueError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            return valor


i = leiaint('Digite um número Inteiro: ')
r = leiareal('Digite um número Real: ')
print(f'Você acabou de digitar o número Inteiro {i} e o número Real {r}.')
