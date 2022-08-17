salary = float(input('Informe o salário para saber o aumento: R$'))

if salary > 1250:
    new_salary = salary + (salary * 0.1)
    print(f'O salário R${salary:.2f} foi acrescido de 10% e o novo salário é R${new_salary:.2f}.')
else:
    new_salary = salary + (salary * 0.15)
    print(f'O salário de R${salary:.2f} foi acrescido de 15% e o novo salário é R${new_salary:.2f}.')
