print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triang')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triang')
