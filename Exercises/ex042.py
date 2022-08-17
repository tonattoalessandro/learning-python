print(f'\033[1;33m▲▼\033[m' * 10)
print('\033[1mTESTE DE TRIÂNGULO\033[m')
print(f'\033[1;33m▲▼\033[m' * 10)

a = float(input('Informe o primeiro segmento de reta: '))
b = float(input('Informe o segundo segmento de reta: '))
c = float(input('Informe o terceiro segmento de reta: '))

if a < b + c and b < a + c and c < a + b:
    print(f'As retas {a}, {b} e {c} \033[1;32mPODEM\033[m formar um triângulo ', end='')
    if a != b and a != c and b != c:
        print('\033[1;34mESCALENO\033[m.')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('\033[1;34mISÓSCELES\033[m.')
    else:
        print('\033[1;34mEQUILÁTERO\033[m.')

else:
    print(f'As retas {a}, {b} e {c} \033[1;31mNÃO PODEM\033[m formar um triângulo!')
