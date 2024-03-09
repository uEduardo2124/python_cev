from ex108 import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.formatar(p)} é {moeda.formatar(moeda.metade(p))}')
print(f'O dobro de {moeda.formatar(p)} é {moeda.formatar(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.formatar(p)}, temos {moeda.formatar(moeda.aumento(p))}')
print(f'Reduzindo 13% de {moeda.formatar(p)}, temos {moeda.formatar(moeda.reduzir(p))}')
