valores = []
par = []
impar = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    continuar = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}') 
print(f'A lista de ímpares é {impar}')
