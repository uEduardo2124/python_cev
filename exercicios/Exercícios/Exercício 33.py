a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
'''maior = 0
menor = v1          # Atribuindo valor á variável menor com o primeiro valor
if v1 > maior:      # Se o valor 1 é maior que a variável "maior"
    maior = v1      # maior recebe o valor 1
if v2 > v1:         # Se o valor 2 é maior que o valor 1
    maior = v2      # maior recebe o valor 2
    menor = v1      # menor recebe o valor 1
else:               # Se valor 2 for menor que o valor 1
    menor = v2      # menor recebe o valor 2
if v3 > maior:      # Se o valor 3 é maior que o maior
    maior = v3      # maior recebe valor 3 caso seja verdadeiro
else:               # caso seja falso, ou seja, maior for maior que valor 3
    if v3 < v2:     # e se valor 3 for menor que valor 2
        menor = v3  # menor recebe valor 3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))'''

# Testando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Testando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor foi \033[32m{}\033[m'.format(menor))
print('O maior valor foi \033[31m{}\033[m'.format(maior))
