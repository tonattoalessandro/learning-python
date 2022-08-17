print('\033[1;32m-=\033[m' * 10)
print('\033[1mCALCULADORA DE MÉDIA\033[m')
print('\033[1;32m-=\033[m' * 10)

first_grade = float(input('Informe a primeira nota do aluno: '))
second_grade = float(input('Informe a segunda nota do aluno: '))

average = (first_grade + second_grade) / 2
print(f'\nMédia {average}')

if average < 5:
    print('\033[1;31mREPROVADO\033[m')
elif average >= 7:
    print('\033[1;32mAPROVADO\033[m')
else:
    print('\033[1;33mRECUPERAÇÃO\033[m')
