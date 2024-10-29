# EXERCICIO 01:
num = int(input('Digite um número de (1 a 10): '))
if num == 1: print('1 -> Um')
elif num == 2:print('2 -> Dois')
elif num == 3:print('3 -> Três')
elif num == 4:print('4 -> Quatro')
elif num == 5:print('5 -> Cinco')
elif num == 6: print('6 -> Seis')
elif num == 7:  print('7 -> Sete')
elif num == 8:print('8 -> Oito')
elif num == 9:print('9 -> Nove')
elif num == 10:print('10 -> Dez')
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
conta_sim = 0
p1 = input('Telefonou para vítima? ').title()
p2 = input('Esteve no local do crime? ').title()
p3 = input('Mora perto da vítima ? ').title()
p4 = input('Devia para vítima? ').title()
p5= input('Já trabalhou com a vítima? ').title()
if p1 == 'Sim':
    conta_sim = conta_sim + 1
if p2 == 'Sim':
    conta_sim = conta_sim + 1
if p3 == 'Sim':
    conta_sim = conta_sim + 1
if p4 == 'Sim':
    conta_sim = conta_sim +1
if p5 == 'Sim':
    conta_sim = conta_sim + 1

if conta_sim == 2:
    print('SUSPEITA')
elif conta_sim == 3 or conta_sim == 4:
    print('CÚMPLICE')
elif conta_sim == 5:
    print('ASSASSINO')
else: print('INOCENTE')

# EXERCICIO 04:
num = int(input('Digite um número até 4 algarismo: '))
milhar = num // 1000 % 10
centena = num // 100 % 10
dezena = num // 10 % 10
unidade = num // 1 % 10
print('A milhar é {}\nA centena é {}\nA dezena é {}\nA unidade é {}'.format(milhar, centena, dezena, unidade))
print('A soma dos algarismo {} + {} + {} + {} é {}'.format(milhar, centena, dezena, unidade, milhar+centena+dezena+unidade))

# EXERCICIO 05:
num = int(input('Digite um número: '))
m_7 = num % 3
m_3 = num % 7
if m_7:
    print('É multiplo de 7')
elif m_3:
    print('É multiplo de 3')
elif m_3 == m_7:
    print('É multiplo de 3 e 7')
else: print('Não é multiplo')


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
num = int(input('Digite um número: '))
milhao = num // 10000 % 10
milhar = num // 1000 % 10
centena = num // 100 % 10
dezena = num // 10 % 10
unidade = num // 1 % 10

print('Milhão', milhao)
print('Milhar', milhar)
print('Centena', centena)
print('Dezena', dezena)
print('Unidade', unidade)

if milhao == unidade and milhar == dezena:
    print('O número digitado é um PALÍNDROMO!')
else: print('O número não é um PALÍNDROMO!')


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








