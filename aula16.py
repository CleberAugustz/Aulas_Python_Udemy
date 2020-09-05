#atribuição adicional
num1 = int(input('Digite um número'))
s = 'par' if num1 % 2 == 0 else 'impar'
print(s)

#compactando esse código
'''num1 = int(input('Digite um número'))
if(num1 % 2 ==0):
    s = 'par'
if(num1 % 2 != 0):
    s = 'impar'
print('Você digitou um valor {}'.format(s))'''