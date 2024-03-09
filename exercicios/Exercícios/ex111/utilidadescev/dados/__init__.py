'''def validar(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
'''
def validar():
    while True:
        num = str(input('Digite um preço: R$')).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[31mERRO! "{num}" é um preço inválido!\033[m')
        else:
            return float(num)
        break