largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
a = (largura * altura)
print('Sua parede tem dimensão {}x{} e sua área é de {}metros quadrados'.format(largura, altura, a))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(a/ 2))