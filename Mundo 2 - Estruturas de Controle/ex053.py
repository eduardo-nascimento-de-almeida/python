# Crie um programa que leia um frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = '''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')