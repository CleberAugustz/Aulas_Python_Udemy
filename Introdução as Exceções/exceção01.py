#coding: utf-8

#author: Cleber Augusto Dias Da Silva

########################
#### Cleber Augusto ####
########################

try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print('Não é possível dividir um número por zero.')

