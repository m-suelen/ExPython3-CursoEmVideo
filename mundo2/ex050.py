"""
Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""


spar = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        spar += n
        cont += 1
print(f'Você informou {cont} números pares é a soma foi {spar}')


