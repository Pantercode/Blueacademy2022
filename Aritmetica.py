#Operações Aritmeticas
# + Adição 5+2 == 7
# - Substração 5-2 == 3
# * Multiplicação 5*2 == 10
# / Divisão 5/2== 2.5
# // Divisão Inteiro 5//2== 2.5 ou como quero inteiro o ser e 5//2==1
# % Resto da Divisão 5%2 == 2
# ** Exponenciação  5**2 == 25 #

#Ordem de precedencia
# 1 () paretenseses
# ** potencia ou exponencia
# *,/,//,% (Multiplicação, Divisão, Divisão de Inteiro e Resto da divisão#


#nome =input('Qual o seu nome:?')
#print('Prazer em te conhecer {:=^50}!'.format(nome))

#nome =input('Qual o seu nome:?')
#print('Prazer em te conhecer {:50}!'.format(nome))

#nome =input('Qual o seu nome:?')
#print('Prazer em te conhecer {:>50}!'.format(nome))

#nome =input('Qual o seu nome:?')
#print('Prazer em te conhecer {:<50}!'.format(nome))

#nome =input('Qual o seu nome:?')
#print('Prazer em te conhecer {:=50}!'.format(nome))#

n1 =int(input('Um valor: '))
n2= int(input('Outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
ep = n1 ** n2
d = n1 / n2
dint = n1 // n2
r = n1 % n2
print('A Soma é {},\n produto é {} e a \n divisão é {:.3f}!'.format(a,m,d), end='')
print('A Divisão inteira é {} e potência {}'.format(dint,ep))
