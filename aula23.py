lista = ['Claudio','José','Maria','Beltrano','Joao','Fulano','Ciclano']
print(lista.reverse())
print(lista.sort())
print(lista.sort(reverse=True))

print(len(lista))
print(lista[len(lista)-1])
print(lista[1])
print(lista.insert(5,'José'))#adicionando um novo elemento.
print(lista.append('José'))
print(lista.count('José'))
print(lista.index('Maria'))
2 in (1,2,3,4,5)
2 not in (1,2,3,4,5)
2 in range(1,6)
list(range(1,6,))
3 and 5 in range(1,6)
((1 and 6) or (5 and 6)) in range(1,6)
((1 and 3) or (5 and 6)) in range(1,6)
(2 or 10) in range(1,6)