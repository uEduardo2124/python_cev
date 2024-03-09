alunos = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()

    continuar = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 40)
print(f'{"No.:<4"}{"NOME:<10"}{"MÉDIA:<8"}')
print('-' * 26)
for c in range(0, len(alunos)):
    print(f'{c:<4}   {alunos[c][0]:<10}       {(alunos[c][1] + alunos[c][2]) / 2:>8.1f}')
print('-' * 35)
while True:
    nota = int(input('Digite o número do aluno que deseja mostrar as notas (999 interrompe): '))
    if nota <= len(alunos) - 1:
        print(f'Notas de {alunos[nota][0]}: {alunos[nota][1]},  {alunos[nota][2]}')
    if nota == 999:
        print('FINALIZANDO...')
        break
print('<<< VOLTE SEMPRE! >>>')
