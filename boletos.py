import random
c1 = str(input('Primeira conta :'))
c2 = str(input('Segunda conta :'))
c3 = str(input('Terceira conta :'))
c4 = str(input('Quarta conta :'))
contas = [c1,c2,c3,c4]
boletos = random.choice(contas)
print('A conta Escolhida foi {}.'.format(boletos))