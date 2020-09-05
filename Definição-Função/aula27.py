# def soma():
#     return 10
# print(soma())
#RETURN SIMPLES
# def soma(x,y):
#     num = x * y
#     return num
#
# print(soma(10,20))
#RETURN DE VALORES MÚLTIPLOS

# def func():
#     return 1,2
#
# a, b = func()
#
# print(a)
# print(b)

def potencia(x):
    quadrado = x**2
    cubo = x**3
    return quadrado, cubo

q, c = potencia(10)
print(q)
print(c)