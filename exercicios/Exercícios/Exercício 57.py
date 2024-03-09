s = str(input('Informe seu sexo [M\F]: ')).strip().upper()
if s != 'M' and s != 'F':
    while s != 'M' and s != 'F':
        s = str(input('\033[31mDados inválidos\033[m. Por favor, informe seu sexo [M\F]: ')).strip().upper()[0]
print('\033[32mSexo {} registrado com sucesso!\033[m'.format(s))
