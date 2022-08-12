days = int(input('O carro foi alugado por quantos dias? '))
km = float(input('O carro rodou quantos quilômetros? '))

days_value = days * 60
km_value = km * 0.15

payment = days_value + km_value

print(f'O valor total a ser pago é de R${payment:.2f}. \nO custo por dia foi de R${days_value:.2f}'
      f'\nE o custo por km rodado foi de R${km_value:.2f}.')
