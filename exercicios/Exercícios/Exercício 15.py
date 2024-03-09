km = float(input('Digite a quantidade de Km percorridos pelo carro: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
total = (km * 0.15) + (dias * 60)
print('O total a pagar foi de: R${:.2f}'.format(total))
