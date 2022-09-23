from time import sleep

first = int(input('Informe o primeiro termo de uma Progressão Aritmética: '))
reason = int(input('Informe a razão da PA: '))
progression = first
elements = 10
counter_elem = elements
counter = 1

while elements != 0:
    while counter <= elements:
        print(progression, end=' ')
        progression += reason
        counter += 1
    sleep(0.5)
    elements = int(input('\nVocê quer ver mais quantos termos? Digite 0 para encerrar: '))
    if elements != 0:
        counter = 1
        counter_elem += elements

print(f'Foram exibidos {counter_elem} elementos da PA.')
