while True:
    print('--' * 20)
    v = int(input('\033[34mDigite o valor que deseja ver a tabuada:\033[m '))
    print('--' * 20)
    if v < 0:
        break
    c = 0
    for c in range(1, 11):
        print(f'\033[35m{v:2} x {c:2} = {v * c:2}\033[m')
print('\033[32mPROGRAMA TABUADA ENCERRADO. volte sempre!\033[m')
