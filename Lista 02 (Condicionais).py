# EXERCICIO 01:
num = int(input('Digite um número de (1 a 10): '))
if num == 1:
    print('1 -> Um')
elif num == 2:
    print('2 -> Dois')
elif num == 3:
    print('3 -> Três')
elif num == 4:
    print('4 -> Quatro')
elif num == 5:
    print('5 -> Cinco')
elif num == 6:
    print('6 -> Seis')
elif num == 7:
    print('7 -> Sete')
elif num == 8:
    print('8 -> Oito')
elif num == 9:
    print('9 -> Nove')
elif num == 10:
    print('10 -> Dez')
else: print('Número Inválido.')

# EXERCICIO 02:
n1 = float(input('Digite sua 1º nota: '))
n2 = float(input('Digite sua 2ºnota: '))
soma = (n1 + n2)/2
if 7 >= soma < 10:
    print('Sua média foi {} - APROVADO!'.format(soma))
elif soma < 7:
    print('Sua média foi {} - REPROVADO!'.format(soma))
elif soma == 10:
    print(' Sua média foi {} - APROVADO COM DISTINÇÃO!'.format(soma))

# EXERCICIO 03:

# EXERCICIO 04:

# EXERCICIO 05:

# EXERCICIO 06:

idade = int(input('Digite sua idade: '))
if 21 <= idade < 65:
    print('Maior de idade.')
elif idade < 21:
    print('Menor de idade.')
elif idade >= 65:
    print('Pessoa idosa.')
    idade = int(input('Digite sua idade: '))

# EXERCICIO 07:

# EXERCICIO 08:
peso = float(input('Digite seu peso em kilos: '))
altura = float(input('Qual é a sua altura em metros: '))
imc = peso/altura**2
if imc < 20:
    print('Abaixo do peso, seu IMC é {:.1f}.'.format(imc))
elif 20 <= imc < 25:
    print('Peso normal,seu IMC é {:.1f}.'.format(imc))
elif 25 <= imc < 30:
    print('Sobre peso.,seu IMC é {:.1f}.'.format(imc))
elif 30 <= imc < 40:
    print('Obeso, seu IMC é {:.1f}.'.format(imc))
elif imc > 40:
    print('Obeso mórbido, seu IMC é {:.1f}.'.format(imc))

# EXERCICIO 09:
idade = int(input('Informe a sua idade: '''))
if idade < 16:
    print('Não eleitor.')
elif 18 < idade < 65:
    print('Eleitor obrigatório.')
elif 16 <= idade <= 18 or idade >= 65:
    print('Eleitor facultativo.')








