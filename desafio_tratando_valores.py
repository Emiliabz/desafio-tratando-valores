"""
DESAFIO: Tratando vários valores - Curso em vídeo
-------------------------------------------------------------------------
Enunciado:
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada (flag).

No final, mostre:
1. Quantos números foram digitados (desconsiderando o flag).
2. Qual foi a soma entre eles (desconsiderando o flag).
-------------------------------------------------------------------------
"""

soma = 0
contador = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))

    if num == 999:
        break

    soma += num
    contador += 1

print(f'\nVocê digitou {contador} números.')
print(f'A soma entre eles foi {soma}.')