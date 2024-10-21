# EXERCICIO 01:
sal_bruto = float(input('Digite seu sálario: R$ '))
vant = float(input('Quanto foi a sua comissão? R$ '))
print('Descontos:')
inss = 5/100
ir = 11/100
fgts = 8/100
conta1 = (sal_bruto+vant) * inss
print('Desconto do INSS é de R${}'.format(conta1))
conta2 = (sal_bruto+vant) * ir
print('Desconto do IR é de R${}'.format(conta2))
conta3 = (sal_bruto+vant) * fgts
print('Desconto do FGTS é de R${}'.format(conta3))
sal_liq = sal_bruto+vant - conta1 - conta2 - conta3
print('O seu salário líquido é de R${}'.format(sal_liq))

# EXERCICIO 02:
qnt_apto = int(input('Quantos apartamentos tem seu condomínio? '))
val_agua = float(input('O valor da água do condomínio foi de R$ '))
val_ener = float(input('Quanto foi o valor da energia do condomínio? R$ '))
rateio = (val_agua+val_ener)/qnt_apto
print('O valor do rateio a ser pago é de R${:.2f}'.format(rateio))

# EXERCICIO 03:
nota1 = float(input('Digite aqui a primeira nota:'))
nota2 = float(input('Digite aqui a segunda nota:'))
conta = (nota1 + nota2)/2
print('A média das notas é de {:.2f}'.format(conta))

# EXERCICIO 04:
sal_bruto = float(input('Digite seu salário: R$ '))
hr = int(input('Quantas horas extras você possui? '))
hora = 5.50
conta = hr*hora + sal_bruto
print('O seu salário junto as horas extras é de R${}'.format(conta))

# Exercicio 05:
sb = float(input('Digite seu salário bruto: R$'))
h_extras = int(input('Quantas horas extras você possui?'))
v_H_extra = h_extras * 9.5
print('O valor da sua hora extra é de R${}'.format(v_H_extra))
comissao = 500
print('O valor de sua comissão fixa é de R${}'.format(comissao))
sal_bru = sb + v_H_extra + comissao
print('O seu salário bruto é de R${}'.format(sal_bru))
ir = 0.05
inss = 0.11
sal_liq = sal_bru * ir
print('Desconto do IR: R${:.2f}'.format(sal_liq))
sal_liq2 = sal_bru * inss
print(('Desconto do INSS: R${:.2f}'.format(sal_liq2)))
calculo_final = sal_bru - sal_liq - sal_liq2
print('Seu salário líquido é de R$ {:.2f}'.format(calculo_final))

# EXERCICIO 06:
dist = float(input('Qual a distancia que você percorreu? '))
comb = float(input('Quantos litros você gastou? '))
media = dist/comb
print('A média de consumo de combustivel foi de {:.2f}Km/l'.format(media))

# EXERCICIO 07:
sal_fixo = float(input('Digite aqui o seu salário: R$ '))
vendas = int(input('Das vendas, qual foi o valor que você faturou? R$ '))
comissao = vendas * 15/100
t_a_receber = sal_fixo + comissao
print('Seu salário líquido é de R${}'.format(t_a_receber))

# EXERCICIO 08:
cand_masculino = int(input('Quantos candidatos masculinos há na sala? '))
cand_feminino = int(input('Quantos candidatos feminino há na sala? '))
cand_ausentes = int(input('Quantos candidatos ausentes há na sala? '))
t_CAND = cand_masculino+cand_feminino+cand_ausentes
print('Total de candidatos inscritos:{}'.format(t_CAND))
t_presente = cand_masculino+cand_feminino
p1 = cand_masculino * 100/t_CAND
p2 = cand_ausentes * 100/t_presente
print('Porcentagem de candidatos homens presentes na sala:{:.1f}%'.format(p1))
print('Porcentagem de candidatos ausentes na sala:{:.1f}%'.format(p2))

# EXERCICIO 09: ERRADO
print('Salário Mínimo: R$ 1.043')
salario = 1.043
taxa_kw = int(input('Seu consumo mensal é de quantos KW? '))
print('O valor de cada quilowatt é de R$1.043')
reais_kw = 1.043 * taxa_kw
print('Seu consumo de energia é de R${:.2f}'.format(reais_kw))
desconto = reais_kw*15/100
print('O valor da conta com 15% de desconto é de R${:.2f}'.format(desconto))
print('O valor da conta com o desconto é de R${:.2f}'.format(reais_kw-desconto))

# EXERCICIO 10:
v_a_hora = int(input('Valor cobrado por hora: '))
qnt_hora = int(input('Quantas horas de duração: '))
valor_show = v_a_hora*qnt_hora
print('Valor do show: R${}'.format(valor_show))
v_km = 50
distancia = float(input('Qual foi a distância percorrida: '))
deslocamento = v_km*distancia
print('O valor do deslocamento é de R${}'.format(deslocamento))
frete = deslocamento*35/100
print('O valor do frete é de R${}'.format(frete))
show = valor_show+deslocamento
print('O valor do show é R${}'.format(show))

# EXERCICIO 11:



























