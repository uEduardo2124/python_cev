#import math
#co = float(input('Comprimento do cateto Oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#h = math.sqrt((co ** 2 + ca ** 2))
#print('A hipotenusa vai medir {:.2f}'.format(h))
import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#h = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(h))

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(co , ca)
print('A hipotenusa vai medir {:.2f}'.format(h))
