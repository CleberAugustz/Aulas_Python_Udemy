lista = [1,2,3,4,5]

#Formas de adicionar elementos
#adiciona o elemento no último indice.
lista = lista + [6]

#adiciona o elemento no inicio indice.
lista = [6] + lista
#ATENÇÃO, SÓ É POSSÍVEL CONTATENAÇÃO ENTRE LISTAS.

#Através do append
#no último indice!
#tambem é possível adicionar uma sublista
lista.append(32)

#adicionar varias vezes um mesmo elemento na lista

lista += 10*[0]

#EXCLUIR ELEMENTO
del(lista[-1])
#nesse formato é exclui o último elemento
