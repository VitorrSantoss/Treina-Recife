# EXERCICIO 01:
d_num = int(input('Digite um número: '))
d_num2 = int(input('Digite outro número: '))
soma = d_num + d_num2
menos = d_num - d_num2
mult = d_num * d_num2
div = d_num / d_num2
print('Coms os números digitados. A soma é {}. A subtração é {}. A ,multiplicação é {}. A divisão é {}.'.format(soma, menos, mult, div))

# EXERCICIO 02:
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print('Os valores de A e B respectivamente é {}, {}.'.format(a, b))
print('Efetuando a troca númerica das variáveis, o valor respectivo de A e B é {}, {}.'.format(b, a))

# EXERCICIO 03:
grau = float(input('Qual é a temperatura em ºC '))
far = (grau * 9/5) + 32
print('A temperatura em fahrenheit é {:.1f}Fº'.format(far))

# EXERCICIO 04:
v_real = float(input('Qual valor a ser convertido? R$ '))
print('A cotação atual é: US$ 1.00 = R$ 5.70')
conversao = v_real / 5.70
print('A sua conversão é de US${:.2f}'.format(conversao))

# EXERCICIO 05:
v_depositado = int(input('Qual valor a ser depositado? R$ '))
juros = 50/100
redimento = v_depositado * juros
print('Seu redinmento foi de R${:.0f}.'.format(redimento))
v_total = redimento + v_depositado
print('Valor total na poupança após o 1º mês. R${:.0f}'.format(v_total))

# EXERCICIO 06:
v_produto = float(input('Valor do produto: R$ '))
prestacao = v_produto / 5
print('O valor das 5 prestações será R$ {}'.format(prestacao))

# EXERCICIO 07:
v_custo = float(input('Qual é o custo do produto? R$ '))
print('A taxa de lucro é de 25%')
t_lucro = 25/100
margem = v_custo*t_lucro
print('O valor da taxa de lucro é {:.2f}'.format(margem))
print('O valor de venda desse produto é de R${}'.format(v_custo+margem))

# EXERCICIO 08:
name = input('Qual é o seu nome? ')
s_fixo = 4550
print('{}, seu salário fixo é de R${}'.format(name, s_fixo))
t_vendas = int(input('Quantas vendas você fez no mês? R$ '))
comissao = t_vendas*15/100
print('Sua comissão é de R${}'.format(comissao))
print('{}, seu salário ao fim do mês é de R${}'.format(name, s_fixo+comissao))

# EXERCICIO 09:
idade = int(input('Qual é a sua idade? '))
dias = idade*365
meses = dias/30
print('Você tem {} anos, {:.0f} meses, {} dias de vida.'.format(idade, meses, dias))

# EXERCICIO 10:
custo_fabrica = float(input('Qual é o custo para se produizr um carro? R$ '))
imposto = custo_fabrica * 48/100
distribuidor =  imposto * 28/100
print('O valor do imposto ao vender o carro é R${:.2f}'.format(imposto))
print('O valor da parte do distrobuidor é R${:.2f}'.format(distribuidor))
print('O valor total do carro ao cliente é de R$ {:.2f}'.format(custo_fabrica + imposto + distribuidor))

# EXERCICIO 11:
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
































