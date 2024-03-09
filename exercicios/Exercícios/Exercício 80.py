'''valores = []
for cont in range(0, 5):
    valor = int(input('Digite um valor: '))
    if cont == 0:
        valores.append(valor)
        print('Adicionado ao final da lista...')
    if cont == 1:
        if valor > valores[0]:
            valores.append(valor)
            print('Adicionado ao final da lista...')
        else:
            valores.insert(0, valor)
            print('Adicionado na posição 0 da lista...')
    if cont == 2:
        if valor < valores[0]:
            valores.insert(0, valor)
            print('Adicionado na posição 0 da lista...')
        elif valor > valores[1]:
            valores.append(valor)
            print('Adicionado ao final da lista...')
        else:
            valores.insert(1, valor)
            print('Adicionado na posição 1 da lista...')
    if cont == 3:
        if valor < valores[0]:
            valores.insert(0, valor)
            print('Adicionado na posição 0 da lista...')
        elif valor > valores[2]:
            valores.append(valor)
            print('Adicionando ao final da lista...')
        elif valor < valores[1] and valor > valores[0]:
            valores.insert(1, valor)
            print('Adicionado na posição 1 da lista...')
        else:
            valores.insert(2, valor)
            print('Adicionado na posição 2 da lista...')
    if cont == 4:
        if valor < valores[0]:
            valores.insert(0, valor)
            print('Adicionado na posição 0 da lista...')
        elif valor > valores[3]:
            valores.append(valor)
            print('Adicionado ao final da lista...')
        elif valor < valores[1] and valor > valores[0]:
            valores.insert(1, valor)
            print('Adicionado na posição 1 da lista...')
        elif valor < valores[2] and valor > valores[1]:
            valores.insert(2, valor)
            print('Adicionado na posição 2 da lista')
        else:
            valores.insert(3, valor)
            print('Adicionado na posição 3 da lista')
print('-=' * 30)
print(f'Os valores digitados foram: {valores}')'''

#Resolução Guanabara
valores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores em ordem foram: {valores}')
