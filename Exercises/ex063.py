number = int(input('Quantos elementos da sequência de Fibonacci você quer ver? '))

first = 0
second = 1
fib = 0
counter = 1

while counter <= number:
    if counter == 1:
        print(first, end=' ')
        counter += 1
    elif counter == 2:
        print(second, end=' ')
        counter += 1
    else:
        fib = first + second
        print(fib, end=' ')
        first = second
        second = fib
        counter += 1

print("\033[1;31mACABOU\033[m")

