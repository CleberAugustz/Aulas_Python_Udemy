# # import math
# # # math.acos()
# #
# #
# # e = math.e  # essa prática melhora a performance do sistema.
# #
# # pi = math.pi
# # print(e)
# print(pi)
#==================================================
#IMPORTAR SIMBOLOS E RENOMEAÇÃO


from math import *

# from math import pi, e
# import math
# e = math.e
# pi = math.pi
#Ambas importações são equivalentes

def func():
    from math import factorial
    print(factorial(10))
func()

from math import sqrt #square

print(sqrt(9))
print(pi,e)

