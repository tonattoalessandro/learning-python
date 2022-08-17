vel = float(input('Qual a velocidade do carro? '))

if vel > 80:
    print('VOCÊ FOI MULTADO!')
    tax = (vel - 80) * 7
    print(f'O valor da multa é R${tax:.2f}.')
