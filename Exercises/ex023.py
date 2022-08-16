number = int(input("Informe um número entre 0 e 9999: "))

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print(f'''Analisando o número {number}...
Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}''')
