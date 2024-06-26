#Programa onde o usuário possa saber a área de um circulo, de um triângulo ou de um trapézio.

#Círculo: raio * PI 3,14
#Triângulo : área do triângulo é o produto entre a base e a altura divido por 2.
#Trapézio: A área do trapézio é a soma das bases vezes a altura dividido por dois.

#Funções
import os
# Usando o Lambda
calcular_circulo = lambda raio, pi: raio * pi

# usando função normal
#def calcular_circulo(raio, pi):
#    area = raio * pi
#    return area

print(f'{'-'*30} CALCULAR A ÁREA DO CIRCULO {'-'*30}')
raio = int(input('Informe o valor do raio: '))
pi = str(input('Informe o valor de PI: ')).replace(',', '.')
pi = float(pi)

#os.system('cls')

print(f'A área do circulo é: {calcular_circulo(raio, pi)}')
print()

calcular_triangulo = lambda base, altura: base * altura /2
#def calcular_triangulo(base, altura):
#    area = base * altura / 2
#    return area

print(f'{'-'*30} CALCULAR A ÁREA DO TRIÂNGULO {'-'*30}')
base = int(input('Informe o valor da base: '))
altura = str(input('Informe o valor da altura: ')).replace(',', '.')
altura = float(altura)

#os.system('cls')

print(f'A área do triângulo é: {calcular_triangulo(base, altura)}')
print()

calcular_trapezio = lambda base1, base2, altura: base1 + base2 * altura /2
#def calcular_trapezio(base1, base2, altura):
#    area = base1 + base2 * altura / 2
#    return area

print(f'{'-'*30} CALCULAR A ÁREA DO TRAPÉZIO {'-'*30}')
base1 = int(input('Informe o valor da 1º base: '))
base2 = int(input('Informe o valor da 2º base: '))
altura = str(input('Informa o valor da altura: ')).replace(',', '.')

altura = float(altura)

#os.system('cls')

print(f'A área do trapézio é: {calcular_trapezio(base1, base2, altura)}')