def notas(* nota, sit = False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param nota: Variável q suporta uma ou mais notas de alunos (aceita várias).
    :param sit: Valor opcional caso se deseje ver qual a situação do aluno baseado na sua média
    :return: Dicionário com várias informações sobre a turma
    '''
    dado = {}
    dado['total'] = len(nota)
    dado['maior'] = max(nota)
    dado['menor'] = min(nota)
    dado['média'] = sum(nota)/ len(nota)
    if sit:
        if dado['média'] >= 7:
            dado['situação'] = 'BOA'
        elif dado['média'] >= 5:
            dado['situação'] = 'RAZOÁVEL'
        else:
            dado['situação'] = 'RUIM'
    return dado


resp = notas(5.5, 2.5, 8.5, sit = True)
print(resp)
#help(notas)
