data = {}
resultado = []
soma = m = 0
while True:
    data.clear()
    data['nome'] = str(input('Nome: '))
    data['idade'] = int(input('Idade: '))
    soma += data['idade']
    while True:
        data['sexo'] = str(input('Sexo [M|F]: ')).strip().upper()[0]
        if data['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas Masculino(M) ou Feminino(F).')
    resultado.append(data.copy())

    while True:
        continuar = str(input('Deseja continuar [S|N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas sim(S) ou não(N).')
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A) Ao todo temos {len(resultado)} pessoas cadastradas.')
m = (soma/ len(resultado))
print(f'B) A média de idade é de {m:5.2F} anos')
print('C) A lista das mulheres cadastradas foi ', end='')
for r in resultado:
    if r['sexo'] == 'F':
        print(f'{r["nome"]}', end=' ')
print()
print(f'D) A lista das pessoas com idade acima da média: ')
for r in resultado:
    if r['idade'] >= m:
        print('     ', end='')
        for k, v in r.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
