sum = 0

for num in range(1, 501):
    if num % 2 != 0:
        if num % 3 == 0:
            sum += num

print(f'A soma dos valores ímpares e múltiplos de 3 no intervalo entre 1 e 500 é {sum}.')
