#coding: utf-8

#author: Cleber Augusto Dias Da Silva

########################
#### Cleber Augusto ####
########################

def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print(type(e))#Instância da exceção
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except (TypeError,NameError)as e:
        print(type(e))#Instância da exceção
    else:
        print("Nenhuma exceção ocorreu.")


erro('int+int')
# #NameError
erro('a')
#ValueError
erro("int('a')")
#ZeroDivisionError
erro("5/0")
erro('10+10')
print('A Aplicação finalizada')
