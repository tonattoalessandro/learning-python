from datetime import date
major = 0
minor = 0

actual_year = date.today().year

for year in range(0, 7):
    born = int(input('Em que ano você nasceu? '))
    if actual_year - born >= 18:
        major += 1
    else:
        minor += 1

print(f'{major} pessoas têm 18 anos ou mais.')
print(f'{minor} pessoas tem menos de 18 anos.')
