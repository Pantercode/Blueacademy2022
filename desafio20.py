import random

al1 = str(input('O Primeiro aluno sorteado foi!'))
al2 = str(input('O Segundo aluno sorteado foi!'))
al3 = str(input('O Terceiro aluno sorteado foi!'))
al4 = str(input('O Quarto aluno sorteado foi!'))
#Resolução
alunos = [al1, al2, al3, al4]
sorteados = random.shuffle(alunos)
print('O alunos da apresentação ')
print(alunos)
