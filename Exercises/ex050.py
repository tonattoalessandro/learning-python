sum = 0

for i in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        sum += num

print(f'A soma dos números pares digitados é {sum}.')
