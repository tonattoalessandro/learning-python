highest = 0
lowest = 0

for i in range(0, 5):
    weight = float(input(f'Informe o {i + 1}° peso em kg: '))
    if i == 0:
        highest = weight
        lowest = weight
    else:
        if weight > highest:
            highest = weight
        elif weight < lowest:
            lowest = weight

print(f'O maior peso digitado foi {highest:.2f} kg.')
print(f'O menor peso digitado foi {lowest:.2f} kg.')
