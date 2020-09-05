
#coding: utf-8

#author: Cleber Augusto Dias Da Silva

########################
#### Cleber Augusto ####
########################

def erro(x):
    try:
        eval(x)
    except ValueError as e: #EM CASO DE ERRO
        print(type(e))#Instância da exceção
    except ZeroDivisionError: #EM CASO DE ERRO
        print('ZeroDivisionError')
    except (TypeError,NameError)as e: #EM CASO DE ERRO
        print(type(e))#Instância da exceção
    else: #EM CASO QUE NÂO HOUVE NEHUM!! ERRO
        print("Nenhuma exceção ocorreu.")
    finally: #SEMPRE SERÁ EXECUTADO
        print("Sempre será executado")

erro('int+int')
# #NameError
erro('a')
#ValueError
erro("int('a')")
#ZeroDivisionError
erro("5/0")
erro('10+10')
print('A Aplicação finalizada')
