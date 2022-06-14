#Insira o salário#
salario = float(input("Digite seu salario "))
#Problema e Resolução#
aumento = salario + (salario*15/100)
print('Seu sálario é de R${} e com o rejuste de 15% vai para R${:.3f}'.format(salario,aumento))