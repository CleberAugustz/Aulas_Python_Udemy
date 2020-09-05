#coding: utf-8

__author__ = 'Cleber Augusto Dias Da Silva'

########################
#### Cleber Augusto ####
########################

class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0 #Adicionado o underline antes do nome do membro, diz ao programador que esse membro é de uso restrito interno do escopo
        self._altura = 0
        self.__var = 0
        self.set_altura(altura)
        self.set_largura(largura)
    def set_altura(self, num):
        if (not(isinstance(num, int)and(num > 0))):
            raise ValueError('Altura é inválida: {}'.format(num))
        self._altura = num
        self.__var = 456
    def set_largura(self, num):
        if (not(isinstance(num, int) and (num > 0))):
            raise ValueError('Largura é inválida: {}'.format(num))
        self._largura = num
    def get_area(self):
        return self._altura * self._largura


r = Retangulo(largura=5, altura=5)
r = Retangulo(largura=5, altura=5)


# Usando o underline antes do nome de membro faz com que o python não exiba o mesmo no code-compile, nos dizendo que o mesmo está com o uso restrito dentro do escopo da instância criada, sendo possível acessar somente internamente.