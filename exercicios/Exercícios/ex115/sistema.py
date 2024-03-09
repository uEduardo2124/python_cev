from time import sleep
from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvídeo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    res = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])

    if res == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif res == 2:
        # Opção de adicionar conteúdo
        titulo('NOVO CADASTRO')
        n = str(input('Nome:  '))
        i = LeiaInt('Idade: ')
        cadastro(arq, n, i)
    elif res == 3:
        titulo('Saindo do sistema. Até logo!')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[m')
    sleep(0.5)
