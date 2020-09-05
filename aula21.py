#não funciona, porque não podemos usar funções matemática encima de lista.
''''lista_nums = [100,200,300,400]
for item in lista_nums:
    item += 1000
    print(item)'''

'''lista_nums = [100,200,300,400,500]
#lista_indice = range(4) # Por padrão é atribuido o valor 0
for item in range(len(lista_nums)): #para simplificar, podemos adicionar o range direto
    lista_nums[item] += 1000
print(lista_nums)'''

#Função de nome enumerate
lista_nums = [100,200,300,400,500]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)
print(idx,item)