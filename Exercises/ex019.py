from random import choice

first = input('Digite o primeiro nome: ')
second = input('Digite o segundo nome: ')
third = input('Digite o terceiro nome: ')
fourth = input('Digite o quarto nome: ')

my_list = [first, second, third, fourth]

chosen = choice(my_list)

print(f'O nome escolhido foi: {chosen.capitalize()}.')
