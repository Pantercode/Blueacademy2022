#Crie um programa que leia o cateto oposto de do cateto adjacente de um tringulo retangulo
#calcule e mostre o cumprimento da hipotenusa.
#hypot usado para calcular hipotenusa

from math import hypot
#Problema
adj = float(input('Digite o comprimento do cateto adjacente!'))
opo = float(input('Digite o comprimento do cateto oposto!'))
#calculo (adj ** 2 + opo **) ** (1/2)
hip = hypot(adj,opo)
print(' O Cateto adjacente tem a medida de {} e o Cateto oposto tem a medida {} então a Hipotenusa '
      'tem a medida de {:.2f}.'.format(adj, opo, hypot(hip)))

