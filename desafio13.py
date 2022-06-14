#Interação do usuário#
produto = float(input('Digite o preço do produto '))

#problema da 5% de desconto em produto
desconto = produto - (produto*5/100)
print('O Valor do produto sem o desconto é R${} já com '
      'o desconto de 5 % o valor sai R${}!'.format(produto,desconto))

