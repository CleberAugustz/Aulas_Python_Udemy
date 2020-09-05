#coding: utf-8

__author__ = 'Cleber Augusto Dias Da Silva'

########################
#### Cleber Augusto ####
########################


class A:
    def __init__(self):
        self._var = 0
    @property
    def var(self):
        print('valor está sendo lido')
        return self._var
    @var.setter
    def var(self, x):
        print('O valor está sendo escrito')
        self._var = x

a = A()
a.var = 10
print(a.var)