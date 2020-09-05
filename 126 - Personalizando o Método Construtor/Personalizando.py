#coding: utf-8

__author__ = 'Cleber Augusto Dias Da Silva'

########################
#### Cleber Augusto ####
########################

class Retangulo:

    def __init__(self, largura, altura):
        self.l = largura
        self.a = altura

    def area(self):
        return self.l * self.a

r = Retangulo(7, 5)

print(r.area())