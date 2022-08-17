from datetime import date

year = int(input('Digite um ano para saber se ele é bissexto. Para saber o ano atual, digite 0: '))

if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} É BISSEXTO!')
else:
    print(f'O ano {year} NÃO É BISSEXTO!')
