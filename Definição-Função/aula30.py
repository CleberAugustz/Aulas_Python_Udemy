# INSTRUÇÃO NONLOCAL
var_local2 = 12
def func():
    var_local = 10
    print(var_local)

    def func_interna():
        global var_local2
        var_local2 += 1
        print(var_local2)
    func_interna()

func()