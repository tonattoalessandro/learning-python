first = float(input('Digite o primeiro comprimento de reta: '))
second = float(input('Digite o segundo comprimento de reta: '))
third = float(input('Digite o terceiro comprimento de reta: '))

if first + second > third and first + third > second and second + third > first:
    print(f'As medidas {first}, {second} e {third} PODEM formar um triângulo!')
else:
    print(f'As medidas {first}, {second} e {third} NÃO PODEM formar um triângulo!')
