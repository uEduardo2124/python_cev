v = float(input('Velocidade do veículo: ')) # Leitura da velocidade
if v > 80:
    print('\033[31mMULTADO!\033[m você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R$\033[31m{:.2f}\033[m'.format((v - 80) * 7))
print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
