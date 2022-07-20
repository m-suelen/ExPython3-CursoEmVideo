"""
Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os
valores pares e ímpares em ordem crescente.
"""


numeros = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('='*30)
print(f'Os numeros pares são {numeros[0]}')
print(f'Os numeros ímpares são {numeros[1]}')

