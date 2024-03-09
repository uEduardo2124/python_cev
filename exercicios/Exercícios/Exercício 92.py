from datetime import datetime
infos = {}
infos['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
infos['idade'] = (datetime.now().year - nasc)

infos['ctps'] = int(input('Carteira de Trabaho (0 não tem): '))
if infos['ctps'] != 0:
    infos['contratação'] = int(input('Ano de contratação: '))
    infos['salário'] = float(input('Salário: R$'))
    infos['aposentadoria'] = (infos['contratação'] + 35) - nasc

print('-=' * 30)
for k, v in infos.items():
    print(f'    - {k} tem o valor {v}')
