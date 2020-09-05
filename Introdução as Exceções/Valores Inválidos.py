#coding: utf-8

#author: Cleber Augusto Dias Da Silva

########################
#### Cleber Augusto ####
########################
def begin():
    global num1,num2
    def input_float(msg):
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print('Número inválido.')


    num1 = input_float('Digite o primeiro número:\n')
    num2 = input_float('Digite o segundo número:\n')

begin()
try:
    print(num1 / num2)
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')
    begin()
