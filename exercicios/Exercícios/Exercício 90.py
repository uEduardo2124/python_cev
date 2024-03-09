estudante = {}
estudante['Nome'] = str(input('Nome: '))
estudante['Média'] = float(input(f'Média de {estudante["Nome"]}: '))
if estudante['Média'] >= 7:
    estudante['Resultado'] = 'Aprovado'
elif 5 <= estudante['Média'] <= 7:
    estudante['Resultado'] = 'Recuperação'
else:
    estudante['Resultado'] = 'Reprovado'
print('-=' * 30)
for k, v in estudante.items():
    print(f'    - {k} é igual a {v}')
