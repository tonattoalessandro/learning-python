distance = float(input('Qual a distância da viagem em km? '))

if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45

print(f'O valor da passagem para {distance} km é R${price:.2f}.')
