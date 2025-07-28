idade = int(input('Digite sua idade: '))
peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

if (idade >= 18 and peso >= 60 and altura >= 1.70):
    print('Você está apto para entrar no Exercito')
else:
    print('Você não está apto para entrar no Exercito')