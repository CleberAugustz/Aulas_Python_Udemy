# def pessoa(nome, sobrenome,idade):
#     print(nome)
#     print(sobrenome)
#     print(idade)
#
# # tupla = 'eXcript','Brasil',20
# # #pessoa(tupla[0],tupla[1],tupla[2])
# # pessoa(*tupla) #dessa forma desempacotamos
#
# d = {'nome':'eXcript','sobrenome':'Brasil', 'idade':20}
# pessoa(**d)



#EXEMPLO DE DESEMPACOTAMENTO

lista = [11,10,12]
tupla = 11,10,12
def func(a, b, c):
    print(a)
    print(b)
    print(c)

# lista.sort()
# func(*lista)


# l = [*tupla]
# l.sort()
# func(l)

func(**dict(zip(('b','a','c'), lista)))