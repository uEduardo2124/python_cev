from ex109 import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.formatar(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {moeda.formatar(p)}, temos {moeda.aumento(p, 10, True)}')
print(f'Reduzindo 13% de {moeda.formatar(p)}, temos {moeda.reduzir(p, 13, True)}')
