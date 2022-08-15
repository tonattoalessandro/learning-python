from math import sin, cos, tan, radians

angle = float(input('Informe o ângulo do triângulo retângulo: '))

rad = radians(angle)

print(f'O seno do ângulo {angle}° é {sin(rad)}. \nO cosseno do ângulo {angle}° é {cos(rad)}.')
print(f'A tangente do ângulo {angle}° é {tan(rad)}.')
