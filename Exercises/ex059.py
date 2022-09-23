from time import sleep

first = float(input('Informe um valor: '))
second = float(input('Informe outro valor: '))
option = 0

while option != 5:
    option = int(input('''[1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair: '''))

    sleep(0.5)

    if option == 1:
        operation = first + second
        print(f'O resultado da soma entre {first} e {second} é {operation}.')
    elif option == 2:
        operation = first * second
        print(f'O resultado da MULTIPLICAÇÃO entre {first} e {second} é {operation}.')
    elif option == 3:
        if first > second:
            print(f'O número {first} é maior que o {second}.')
        else:
            print(f'O número {second} é maior que o {first}.')
    elif option == 4:
        first = float(input('Informe um valor: '))
        second = float(input('Informe outro valor: '))

    sleep(0.5)
