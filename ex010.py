#Conversor de temperatura#
#Interaçai do Usuario#
celsius = float(input('Informe a temperatura em °C'))
#Calculo#
#Outra forma de calcular fahrenheit = ((9*celsius)/5)+32 #
fahrenheit = (celsius * 9/5) + 32
#Resolução do problema#
print('Você digitou em {}°C que resultou em {}°F'.format(celsius,fahrenheit))