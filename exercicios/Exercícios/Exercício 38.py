a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a > b:
    print('O \033[31mPRIMEIRO\033[m valor é MAIOR')
elif b > a:
    print('O \033[32mSEGUNDO\033[m valor é MAIOR')
else:
    print('Os valores são \033[35mIGUAIS\033[m')
