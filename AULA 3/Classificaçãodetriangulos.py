lado1 = int(input('Digite o valor do lado 1: '))
lado2 = int(input('Digite o valor do lado 2: '))
lado3 = int(input('Digite o valor do lado 3: '))

if lado1 == lado2 and lado2 == lado3 and lado3 == lado1: #Se todos os lados são iguais
    print('O triângulo é Equilátero')
elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print('O triângulo é Escaleno')
else:
    print('O triângulo é Isósceles')