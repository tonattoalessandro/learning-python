import random

name1 = input('Digite o primeiro nome: ')
name2 = input('Digite o segundo nome: ')
name3 = input('Digite o terceiro nome: ')
name4 = input('Digite o quarto nome: ')

student_list = [name1, name2, name3, name4]

random.shuffle(student_list)

print(f'A ordem de apresentação é {student_list}.')
