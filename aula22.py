''''lista ='Bem-Vindo ao Curso de Python'
print(lista[10])
print(lista[20])
print(lista[:20])
print(lista[10:20])#inicio no 10 e o fim no 20
print(lista[::2])#saltará conforme o último comando.
print(lista[::-1])#ele inverte a frase, porque ele pula de -1 <<'''
l = ['aaa','bbb','ccc']
print(l[1])#é impresso o indice de valor 1
#RESSALTA QUE O PRIMEIRO VALOR É O ZERO
print(l[0])
l.append('eee')#insere elemento no último indice da lista
l.insert(0,'aaa2')#dessa forma é possivel
l[1] = 'bbbbb'
l.clear()
l.pop()
l.pop(0)
del(l[0:2])
del(l[0:4:2])