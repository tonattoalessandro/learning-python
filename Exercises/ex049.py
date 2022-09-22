num = int(input('Digite um número inteiro para saber sua tabuada até o 10° elemento: '))

for i in range(1, 11):
    print(f'{num} X {i:2} = {num * i}')
