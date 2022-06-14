#Aluguel De carro #

#Interação  com o usuario#
dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
#Problema#
alug = (dias * 60) + (km * 0.15)
#Resolução do problema#
print('O carro foi alugado por {}dias e rodou {}Km finalizando o aluguel ficou em R${}.'.format(dias, km, alug))

