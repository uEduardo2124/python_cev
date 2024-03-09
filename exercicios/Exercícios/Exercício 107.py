from ex107 import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10% de R${p}, temos R${moeda.aumento(p, 10)}')
print(f'Reduzindo 13% de R${p}, temos R${moeda.reduzir(p, 13)}')
