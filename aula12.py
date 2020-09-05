'''i = int(input('Informe sua idade?\n'))
if (i <= 0):
    print('A sua idade não pode ser 0 ou menor do que 0!')
else:
    if(i>150):
        print('Sua idade não pode ser super a 150 ano!')
    else:
        if(i<18):
            print('Você precisa ter mais de 18 anos')'''
i = int(input('Informe sua idade?\n'))
if(i<=0):
    print('A sua idade não pode ser 0 ou menor do que 0!')
elif(i>150):
    print('A sua idade não pode ser superior a 150 anos!')
else:
    if(i<18):
        print('Você precisa ter mais do que 18 naos!')
    else:
        (i>18)
        print('\033[2;33;42m Você pode participar \o/')
