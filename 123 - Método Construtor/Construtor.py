#coding: utf-8

__author__ = 'Cleber Augusto Dias Da Silva'

########################
#### Cleber Augusto ####
########################

def teste(s):
    print(id(s))


class A:

    def __init__(self):
        print(id(self))

a = A()
print(id(a))


