contasim = 0
p = input('Telefonou para vítima? ')
if p == 'sim':
    contasim = contasim + 1
p2 = input('Esteve no local do crime? ')
if p2 == 'sim':
    contasim = contasim + 1
p3 = input('Mora perto da vítima? ')
if p3 == 'sim':
    contasim = contasim + 1
p4 = input('Devia para vítima? ')
if p4 == 'sim':
    contasim = contasim + 1
p5 = input('Já trabalhou com a vítima? ')
if p5 == 'sim':
    contasim = contasim + 1
if contasim == 2:
    print('SUSPEITA')
elif contasim == 3 or contasim == 4:
    print('ASSASINO')
else: print('INOCENTE')