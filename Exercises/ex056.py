minor_women = 0
average = 0
older_man = ''
older_age = 0

for i in range(0, 4):
    name = input(f'Qual é o {i + 1}° nome? ').strip().capitalize()
    gender = input('Digite H para HOMEM e M para MULHER: ').strip().upper()
    age = int(input('Quantos anos você tem? '))
    if gender == 'H':
        if age > older_age:
            older_age = age
            older_man = name
    else:
        if age < 20:
            minor_women += 1
    average += age

average = average / 4

print(f'A média de idade do grupo é {average:.2f}.')
print(f'A quantidade de mulheres com menos de 20 anos é {minor_women}.')
if not older_man:
    print('Não foram digitados nomes de Homem.')
else:
    print(f'O nome do homem mais velho é {older_man}.')
