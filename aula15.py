n1 = int(input('Digite um valor:\n'))

if(n1 > 10):
    print('O valor maior que 10!')
    if(n1<=15):
        print('O valor é maior que 10 e menor que 15')
    else:
        if(n1<=50):
            print('O Valor é maior que 10, mas menor do que 50')
        else:
            print('O Valor é maior do que 50')
else:
    if(n1 > 5):
        print('O número é menor do que 10, mas maior que 5')
        if(n1==7):
            print('O número é igual a 7.')
    else:
        print('O valor é menor do que 5.')

d = 1