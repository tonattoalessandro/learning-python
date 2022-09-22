first = int(input('Informe o primeiro termo de uma Progressão Aritmética: '))
reason = int(input('Digite a razão da PA: '))

for i in range(0, 10):
    print(first, end=' → ')
    first += reason

print('ACABOU')
