# calculando o angulo seno, cosseno e tangente
from math import radians, sin, cos, tan
#problema
angulo = float(input('Digite o angulo que você deseja '))
seno = sin(radians(angulo))
cosseno = cos(sin(angulo))
tangente = tan(math.sin(angulo))
#Resolução
print('O ângulo de {} tem o Seno de {:.2f}.'.format(angulo,seno))
print('O ângulo de {} tem o Cosseno de {:.2f}.'.format(angulo,cosseno))
print('O ângulo de {} tem a Tangente de {:.2f}.'.format(angulo,tangente))