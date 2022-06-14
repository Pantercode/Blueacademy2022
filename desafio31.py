from random import randint

computador = randint(0, 5)#Induz o computador a pensar
print('-=-' * 18)
print('Vou pensan em um numero entre 0 a 5 Tente adivinhar...')
print('-=-' * 18)
jogador = int(input('Qual foi o número que pensei? '))#Jogador tentando adivinhar
print('Estou Analisando.....')
if jogador == computador:
    print('PARABÉNS!!     Você me Venceu!!')

else:
    jogador != computador
    print('ERROU!!')
    print('Eu ganhei eu pensei no {}!!!'.format(computador,jogador))
print('-=-' * 18)
print('____________________________Fim______________________')
print('-=-' * 18)