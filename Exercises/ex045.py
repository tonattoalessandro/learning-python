from emoji import emojize
from time import sleep
from random import randint

print('\033[1;33m=-\033[m' * 15)
print(emojize('JO KEN PÔ :facepunch: :hand: :v:', language='alias'))
print('\033[1;33m=-\033[m' * 15)

options = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}

user = int(input('''Escolha uma das opções abaixo para jogar JO KEN PÔ contra o PC:
1 - PEDRA
2 - PAPEL
3 - TESOURA: '''))

pc = randint(1, 3)

print('JOGANDO...')
sleep(1.5)

if user == 1:
    if pc == 1:
        print(f'EMPATE! Você escolheu {options[user]} e o PC também selecionou {options[pc]}.')
    elif pc == 2:
        print(f'DERROTA! Você escolheu {options[user]} e o PC selecionou {options[pc]}.')
    else:
        print(f'VITÓRIA! Você escolheu {options[user]} e o PC selecionou {options[pc]}')
elif user == 2:
    if pc == 1:
        print(f'VITÓRIA! Você escolheu {options[user]} e o PC selecionou {options[pc]}.')
    elif pc == 2:
        print(f'EMPATE! Você escolheu {options[user]} e o PC selecionou {options[pc]}.')
    else:
        print(f'DERROTA! Você escolheu {options[user]} e o PC selecionou {options[pc]}.')
elif user == 3:
    if pc == 1:
        print(f'DERROTA! Você selecionou {options[user]} e o PC selecionou {options[pc]}.')
    elif pc == 2:
        print(f'VITÓRIA! Você escolheu {options[user]} e o PC selecionou {options[pc]}.')
    else:
        print(f'EMPATE! Você escolheu {options[user]} e o PC selecionou {options[pc]}.')
else:
    print(f'ERRO! A opção {user} é inválida!')
