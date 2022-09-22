from time import sleep

number = int(input('Digite um número inteiro: '))
option = int(input(f"""Escolha uma opção de conversão para o número {number}:
1 - binário
2 - octal
3 - hexadecimal: """))

print(f'\033[1;34mProcessando...\033[m')
sleep(1.5)

if option == 1:
    converted = bin(number)[2:]
    print(f'O número \033[1;32m{number}\033[m convetido para base binária é \033[1;32m{converted}\033[m.')
elif option == 2:
    converted = oct(number)[2:]
    print(f'O número \033[1;32m{number}\033[m convertido para base octal é \033[1;32m{converted}\033[m.')
elif option == 3:
    converted = hex(number)[2:]
    print(f'O número \033[1;32m{number}\033[m convertido para base hexadecimal é \033[1;32m{converted}\033[m.')
else:
    print(f'\033[1;31mERRO!\033[m A opção {option} \033[1;31mNÃO é válida!')
