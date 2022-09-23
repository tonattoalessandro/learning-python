from random import randint

computer = randint(0, 10)

user = 11
counter = 0

while user != computer:
    user = int(input('Digite um número inteiro de 0 a 10 para adivinhar o escolhido pelo computador: '))
    counter += 1

print(f'Você acertou! O número escolhido pelo PC foi {computer}, e você precisou de {counter} tentativas!')
