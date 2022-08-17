from time import sleep

print('\033[1;33m-=' * 15)
print(f'AVALIAÇÃO DE EMPRÉSTIMOS')
print('\033[1;33m-=\033[m' * 15)

house = float(input('Qual o valor da casa? R$'))
salary = float(input('Qual o salário do comprador? R$'))
years = int(input('Em quantos anos pretende pagar o imóvel? '))

installment = house / years / 12

print('\n\033[1;34mAnalisando...\033[m\n')
sleep(1.5)

if installment > salary * 0.3:
    print(f'Empréstimo \033[1;31mNEGADO\033[m! A parcela de R${installment:.2f} excede 30% do salário de R${salary:.2f}.')
else:
    print(f'Empréstimo \033[1;32mAPROVADO\033[m! A parcela de R${installment:.2f} é menor que 30% do salário de R${salary:.2f}.')

