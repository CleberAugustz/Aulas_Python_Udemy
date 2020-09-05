# lista_nums = [100,200,300,400]
# for item in lista_nums:
#     print(item+100)
#

#ADICIONANDO UM VALOR AO MESMO-- UTILIZANDO RANGE
# lista_nums = [100,200,300,400,299]
# for item in range(len(lista_nums)):
#     lista_nums[item] += 1000
# print(lista_nums)

#UTILIZANDO ENUMERATE
lista_nums = [100,200,300,400,299]
for idx, item in enumerate(lista_nums):
    lista_nums[idx] += 1000
print(lista_nums)