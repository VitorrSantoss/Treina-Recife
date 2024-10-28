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

# EXERCICIO 12:
peso = float(input('Qual é o peso dos peixes: '))
if peso > 50:
    print('Peso excedido: {:.2f}kg'.format(peso-50))
    print('A multa a ser paga pelo excesso de peso será: R${:.2f}'.format((peso-50)*4))
elif peso < 50:
    print('Peso OK. Sem multas a pagar.')

# EXERCICIO 13:
salario = float(input('Digite aqui seu salário: '))
if salario < 1100:
    print('Seu aumento é de R${}, totalizando R${}'.format(salario * 10 / 100, (salario * 10 / 100) + salario))
elif salario > 1100  <= 2000:
    print('Seu aumento é de R${}, totalizando R${}'.format(salario * 7 / 100, (salario * 7 / 100) + salario))
elif salario > 2000:
    print('O seu aumento é de R${}, totalizando R${}'.format(salario * 5 / 100, (salario * 5 / 100) + salario))

# EXERCICIO 14:
rh = float(input('Digite sua renda: R$ '))
rm = float(input('Digite sua renda: R$ '))
rc = rh + rm
if rc <= 900:
    print('Renda bruta: R${}'.format(rc))               # eu sei que assim é a melhor forma -> rc <=1500 and rc >=901
    print('Insento de IR.')                             #                                      rc <=2500 and rc >=1501
    print('Renda líquida: R${}'.format(rc))
elif 901 <= rc <= 1500:                                 # pq o cód só funciona assim? -> <=1500 >= 901
    print('Renda bruta: R${}'.format(rc))
    print('IR -> 10% -> R${}'.format(rc*10/100))
    print('Renda líquida: R${}'.format(rc-(rc*10/100)))
elif 1501 <= rc <= 2500:                                 # pq o cód só funciona assim? -> <=2500 >=1501
    print('Renda bruta: R${}'.format(rc))
    print('IR -> 15% -> R${}'.format(rc*15/100))
    print('Renda  líquida: R${}'.format(rc-(rc*15/100)))
elif rc > 2500:
    print('Renda bruta: R${}'.format(rc))
    print('IR -> 25% -> R${}'.format(rc*25/100))
    print('Renda líquida: R${}'.format(rc-(rc*25/100)))

# EXERCICIO 15:
saldo_medio = float(input('Digite seu saldo: R$ '))
if saldo_medio <= 500:
    print('Não receberá crédito.')
elif saldo_medio >= 501 and saldo_medio <= 1000:
    print('Receberá um crédito de 30%')
    print('Valor do crédito: R${}'.format(saldo_medio*30/100))
elif saldo_medio >= 1001 and saldo_medio <= 3000:
    print('Receberá um crédito de 40%')
    print('Valor do crédito: R${}'.format(saldo_medio * 40 / 100))
elif saldo_medio > 3001:
    print('Receberá um crédito de 50%')
    print('Valor do crédito: R${}'.format(saldo_medio * 50 / 100))












# EXERCICIOS EXEMPLOS CONDICIONAIS:

#EXEMPLO 01:
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
if v1>10:
    print('A soma é:',v1+v2)
print('A multiplicação é:',v1*v2)

#EXEMPLO 02:
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
if v1 > v2:
    print('A soma vale:',v1+v2)
else:
    print('A multiplicação é:',v1*v2)

#EXEMPLO 03:
idade = int(input('Qual é a sua idade: '))
sexo = input('Qual é o seu sexo - (F) ou (M): ')
salario = float(input('Qual é o seu salário: '))
if idade > 30:
    if sexo=='M' and salario > 3000:
        print('O salário não será reajustado.')
    else:
        if sexo=='M' and salario <= 3000:
            print('O reajuste do salário será: R${}'.format((salario*30/100)+salario))
        else:
            if sexo=='F':
                print('O salário reajustado será: R${}'.format((salario*50/100)+salario))
else:
        if idade < 30:
            if sexo=='F':
                print('O salário reajustado será: R${}'.format((salario*40/100)+salario))
            else:
                if sexo=='M':
                    print('O salário reajustado será: R${}'.format((salario*20/100)+salario))
print('fim do comando')


#EXEMPLO 04:
mes = int(input('Informe o mês (1 a 12): '))
if mes ==1:
    print('JANEIRO')
else:
    if mes ==2:
        print('FEVEREIRO')
    else:
        if mes ==3:
            print('MARÇO')
        else:
            if mes ==4:
                print('ABRIL')
            else:
                if mes==5:
                    print('MAIO')
                else:
                    if mes==6:
                        print('JUNHO')
                    else:
                        if mes==7:
                            print('JULHO')
                        else:
                            if mes==8:
                                print('AGOSTO')
                            else:
                                if mes==9:
                                    print('SETEMBRO')
                                else:
                                    if mes==10:
                                        print('OUTUBRO')
                                    else:
                                        if mes==11:
                                            print('NOVEMBRO')
                                        else:
                                            if mes==12:
                                                print('DEZEMBRO')
                                            else:
                                                print('MÊS INVÁLIDO')
# OU
mes = int(input('Digite o mês (1 a 12): '))
if mes==1: print('Janeiro')
elif mes==2: print('Fevereiro')
elif mes==3: print('Março')
elif mes==4: print('Abril')
elif mes==5: print('Maio')
elif mes==6: print('Junho')
elif mes==7: print('Julho')
elif mes==8: print('Agosto')
elif mes==9: print('Setembro')
elif mes==10: print('Outubro')
elif mes==11: print('Novembro')
elif mes==12: print('Dezembro')
else: print('Mes inválido')

#EXEMPLO 05:
nota = float(input('Digite uma nota: '))
if nota >= 9:
    print('CONCEITO: A')
elif nota >= 8 < 9:
    print('CONCEITO: B')
elif nota >= 7 < 8:
    print('CONCEITO: C')
elif nota < 7:
    print('CONCEITO: D')
else: print('continue codando')

















































