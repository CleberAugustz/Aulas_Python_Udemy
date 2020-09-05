# a = 10
# b = 25
# c = 66
#
# x = int(input('Digite um número:\n'))
# #if (x == a or x == b or x == c):
# if(x in [a,b,c]):
#     print('Está contido.')
# else:
#     print('Não está contido.')


#------------------------------------
cores = ['azul','amarelo','vermelho','branco']

while True:
    cor = input('Digite o nome de uma cor ou então,\n0 para sair do programa:\n').lower()
    if(cor=='0'):
        break
    elif cor in cores:
        print('Essa cor está contida')
    else:
        print('Essa cor não está contida!')
    print()