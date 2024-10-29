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






