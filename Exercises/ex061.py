first = int(input('Digite o primeiro termo de uma Progressão Aritmética: '))
reason = int(input('Informe a razão dessa PA: '))

progression = first

counter = 1
while counter <= 10:
    print(progression, end=' ► ')
    progression += reason
    counter += 1

print("\033[1;33mFIM!")
