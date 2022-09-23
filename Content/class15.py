number = total = 0

while True:
    number = int(input('Digite um número inteiro: '))
    if number == 999:
        break
    total += number
print(f'A soma dos valores digitados é {total}.')
