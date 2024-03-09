maior = homem = mulher = 0
while True:
    print('--' * 15)
    print('    CADASTRE UMA PESSOA     ')
    print('--' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M|F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    print('--' * 15)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'\033[35mTotal de pessoas com mais de 18 anos: {maior}\033[m')
print(f'\033[32mAo todo temos {homem} homem(ns) cadastrados.\033[m')
print(f'\033[34mE temos {mulher} mulher(es) com menos de 20 anos.\033[m')
