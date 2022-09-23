option = 'Ss'
average = tot_sum = highest = lowest = counter = 0

while option in 'Ss':
    number = float(input('Digite um número: '))
    counter += 1
    if counter == 1:
        highest = number
        lowest = number
    else:
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
    tot_sum += number

    option = input('Você quer continuar? Digite S para continuar: ').strip()[0]

average = tot_sum / counter

print(f'A média dos valores digitados foi {average:.2f}.')
print(f'O maior valor digitado foi {highest} e o menor valor foi {lowest}.')
