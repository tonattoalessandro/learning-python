number = int(input('Informe um número inteiro: '))

counter = 0

if number == 1 or number == 2:
    print(f'O número {number} NÃO é primo.')
else:
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1

    if counter > 2:
        print(f'O número {number} NÃO é primo!')
    else:
        print(f'O número {number} é primo.')
