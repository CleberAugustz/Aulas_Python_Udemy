#coding: utf-8

__author__ = 'Cleber Augusto Dias Da Silva'

########################
#### Cleber Augusto ####
########################

class Retangulo:

    def __init__(self):
        self.a = 0
        self.l = 0

    def area(self):
        return self.a * self.l

r1 = Retangulo()
r1.l = 10
r1.a = 5

print(r1.area())
