import math

ca = float(input('Informe o valor do cateto adjacente: '))
co = float(input('Informe o valor do cateto oposto: '))

h = math.sqrt(pow(ca, 2) + pow(co, 2))

print(f'A hipotenusa deste triângulo é {h}')
