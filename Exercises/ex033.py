first = int(input('Digite um número inteiro: '))
second = int(input('Digite outro número inteiro: '))
third = int(input('Digite mais um número inteiro: '))

if first > second and first > third:
    bigger = first
elif second > third:
    bigger = second
else:
    bigger = third

if first < second and first < third:
    smaller = first
elif second < third:
    smaller = second
else:
    smaller = third

print(f'O maior número digitado foi {bigger} e o menor {smaller}.')
