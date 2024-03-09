print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triang', end= '')
    if a == b == c:
        print(' \033[35mEQUILÀTERO\033[m')
    elif a != b != c != a:
        print(' \033[36mESCALENO\033[M')
    else:
        print(' \033[37mISÒSCELES\033[m')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triang')
