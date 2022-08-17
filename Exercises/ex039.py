from datetime import date
print('\033[1;33m-=\033[m' * 15)
print('\033[1mVERIFICADOR DE ALISTAMENTO\033[m')
print('\033[1;33m-=\033[m' * 15)

year = int(input('\nInforme o ano de nascimento: '))

age = date.today().year - year

if age < 18:
    print(f'Você ainda não precisa se alistar. Faltam {18 - age} ano(s) para que você se aliste.')
elif age > 18:
    print(f'O momento de se alistar já passou! Você deveria ter se alistado há {age - 18} ano(s).')
else:
    print(f'Este é o ano do teu alistamento!')
