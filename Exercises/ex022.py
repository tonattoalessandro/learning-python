name = input('Digite seu nome completo: ')

name = name.strip()

print(f'O nome em letras maiúsculas é: {name.upper()}')
print(f'O nome em letras minúsculas é: {name.lower()}')

print(f'O nome completo tem {len(name.replace(" ", ""))} letras.')


print(f'O primeiro nome tem {len(name.split()[0])} letras.')    
