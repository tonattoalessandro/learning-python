from random import randint
from time import sleep

number = randint(0, 5)
print('-----Adivinhe o número!-----')
user_num = int(input('Digite um número entre 0 e 5 para adivinhar o número escolhido pelo computador: '))
print('Vamos ver...\n')
sleep(3)

if user_num == number:
    print("VOCÊ ACERTOU!")
else:
    print('Ahhhh... você errou...')

print(f'O número escolhido pelo computador foi {number}.')
