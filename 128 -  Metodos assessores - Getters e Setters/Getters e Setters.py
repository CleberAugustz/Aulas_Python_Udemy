#coding: utf-8

__author__ = 'Cleber Augusto Dias Da Silva'

########################
#### Cleber Augusto ####
########################


class Retangulo:

    def __init__(self, largura, altura):
        self.largura =  0
        self.altura = 0
        self.set_altura(altura)
        self.set_largura(largura)
    def set_altura(self, num):
        if (not(isinstance(num, int)and(num > 0))): #verifica ao contrário, caso não seja, será exibida o erro e a mensagem personalizada
            raise ValueError('Altura é inválida: {}'.format(num)) #nesse formato , será exibida a mensagem de erro e após a execução é finalizada
        self.altura = num #associa o valor que self.altura irá receber a variável num
    def set_largura(self, num): # recebe uma informação (valores)
        if (not(isinstance(num, int) and (num > 0))): #verifica ao contrário, caso não seja, será exibida o erro e a mensagem personalizada
            raise ValueError('Largura é inválida: {}'.format(num)) #nesse formato , será exibida a mensagem de erro e após a execução é finalizada
        self.largura = num #associa o valor que self.largura irá receber a variável num
    def get_area(self): # retorna um resultado (Valor)
        return self.altura * self.largura


#r = Retangulo(largura=10, altura=5)
r = Retangulo(largura=-5, altura=5)