#Incluir, alterar, excluir elementos

l =  ["aaa","bbb","ccc","ddd",]

print(l[1])

#inserir
l.append("eee")

print(l[-1])

#inseriri de forma especifica conforme o indice
l.insert(0, "bbbbb")

#Altera um elemento da lista
l[1] = "xxxx" #Basta colocar o nome da lista o indice

#Apagar elementos ou uma sequência

l.clear() #ELIMINA TODOS OS ITENS
l =  ["aaa","bbb","ccc","ddd",]

#EXCLUIR O ÚLTIMO ELEMENTO DA LISTA

l.pop()

#SELECIONAR UM ELEMENTO PARA SER EXCLUIDO
l.pop(1)

#EXCLUIR VARIOS ITENS

del(l[2:4]) #nesse caso, irá excluir todos os elementos entre o 2 e o quadro
del(l[::2]) #Exclui pulando de dois em dois



