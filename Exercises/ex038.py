first_number = int(input('Digite um número: '))
second_number = int(input('Digite outro número: '))

if first_number > second_number:
    print(f'O primeiro número digitado é maior que o segundo.')
elif second_number > first_number:
    print(f'O segundo número digitado é maior que o primeiro.')
else:
    print(f'O mesmo número foi digitado duas vezes!')
