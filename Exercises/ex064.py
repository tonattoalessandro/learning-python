number = 0
counter = 0
tot_sum = 0

while number != 999:
    number = int(input('Digite um número inteiro. Para encerrar digite 999: '))
    if number != 999:
        counter += 1
        tot_sum += number

print(f'Foram digitados {counter} números inteiros. A soma entre eles é {tot_sum}.')
