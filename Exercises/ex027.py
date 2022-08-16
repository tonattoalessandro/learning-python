name = input('Digite seu nome completo: ').strip()

splitted_name = name.split()

first_name = splitted_name[0]
last_name = splitted_name[-1]

print(f'''Primeiro nome: {first_name.capitalize()}
Último nome: {last_name.capitalize()}''')
