from datetime import date

print('\033[1;34m-=\033[m' * 16)
print('\033[1;33mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('\033[1;34m-=\033[m' * 16)

year_born = int(input('Digite o ano de nascimento do atleta (YYYY): '))

age = date.today().year - year_born

print(f'IDADE: {age} anos.')
if age <= 9:
    print(f'Categoria: \033[1;35mMIRIM\033[m')
elif age <= 14:
    print(f'Categoria: \033[1;35mINFANTIL\033[m')
elif age <= 19:
    print(f'Categoria: \033[1;35mJÚNIOR\033[m')
elif age == 20:
    print(f'Categoria: \033[1;35mSÊNIOR\033[m')
else:
    print(f'Categoria: \033[1;35mMASTER\033[m')
