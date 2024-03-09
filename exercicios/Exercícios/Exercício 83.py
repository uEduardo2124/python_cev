'''q1 = q2 = 0
ex = [str(input('Digite a expressão: '))]
for cont in ex:
    for c in cont:
        if c == "(":
            q1 += 1
        elif c == ")":
            q2 += 1
if q1 == q2:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')'''

#Resolução Guanabara
ex = [str(input('Digite a expressão: '))]
pilha = []
for simb in ex:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('Sua expressão está válida!' if len(pilha) == 0 else 'Sua expressão está inválida')
