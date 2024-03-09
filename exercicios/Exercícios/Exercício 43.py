p = float(input('Digite o seu peso(Kg): '))
a = float(input('Digite a sua altura(m): '))
imc = (p / a ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[31mABAIXO\033[m do peso normal.')
elif imc < 25:
    print('Parabéns,você está com peso \033[32mIDEAL\033[m.')
elif imc < 30:
    print('Você está em \033[34mSOBREPESO\033[m.')
elif imc < 40:
    print('Você está em \033[33mOBESIDADE\033[m, cuidado!')
else:
    print('Você está em \033[31mOBESIDADE MÓRBIDA\033[m, cuidado!')
