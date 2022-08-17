from time import sleep

print('\033[1;34m-=\033[m' * 7)
print("\033[1mCÁLCULO DE IMC\033[m")
print('\033[1;34m-=\033[m' * 7)

height = float(input('Informe sua altura em metros: '))
weight = float(input('Informe seu peso em kg: '))

bmi = weight / (height ** 2)

print(f'\nO IMC é de {bmi:.1f}. Isso significa...')
sleep(1.5)

if bmi < 18.5:
    print('\033[1;31mABAIXO DO PESO\033[m')
elif bmi < 25:
    print('\033[1;32mPESO IDEAL\033[m')
elif bmi < 30:
    print('\033[1;33mSOBREPESO\033[m')
elif bmi <= 40:
    print('\033[1;31mOBESIDADE\033[m')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA\033[m')
