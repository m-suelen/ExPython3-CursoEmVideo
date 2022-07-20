"""
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
"""


from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))  # radians converte graus em radiando
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de \033[1;31m{angulo}\033[m tem o SENO de \033[4;34m{seno:.2f}\033[m')
print(f'O ângulo de \033[1;31m{angulo}\033[m tem o COSSENO de \033[4;34m{cosseno:.2f}\033[m')
print(f'O ângulo de \033[1;31m{angulo}\033[m tem a TANGENTE de \033[4;34m{tangente:.2f}\033[m')
