#coding: utf-8

#author: Cleber Augusto Dias Da Silva

########################
#### Cleber Augusto ####
########################

def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print('ValueError')
        print(type(e))#Instância da exceção
        print(e.args)#Argumentos as mensagens
        print(e)#___STR____ Mensagem
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except (TypeError,NameError)as e:
        print('NameError ou TypeError')
        print(type(e))#Instância da exceção
        print(e.args)#Argumentos as mensagens
        print(e)#___STR____ Mensagem


# #TypeError
erro('int+int')
# #NameError
erro('a')
#ValueError
# erro("int('a')")
#ZeroDivisionError
# erro("5/0")
# erro('10+10')
print('A Aplicação finalizada')