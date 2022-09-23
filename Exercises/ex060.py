number = int(input('Informe um número inteiro para conhecer seu fatorial: '))
fact = number

if number > 0:
    counter = number - 1
    while counter >= 1:
        fact *= counter
        counter -= 1

print(f'O fatorial de {number} é {fact}.')
