# Escreva um programa que leia um número n inteiro qualquer.
# Mostre na tela os n primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end= ' ')
cont = 3
while cont <= n:  
    t3 = t1 + t2
    print(f'-> {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('-> \033[1;31mFIM!\033[m')