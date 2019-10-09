
#！！！ LEGB(local,enclosed,global,built-in)，就好像环境变量检索的顺序
locals() is globals()
#进入一个函数，产生一个locals()
g_1='global value in Global'

def func1():
    print(locals() is globals())#此时的loclas()就仅指func1内
    func1_name='local values in func1'
    print('locals in func1: ', locals())
    return locals() is globals()

func1()

__builtins__.value1='B value stored in __builtins__'#B，如何定义built-in变量
value1='G value stored in Global'#G，如何定义global变量


# 而当出现嵌套函数inner时，也会新产生一个locals()，而如果inner此时还引用了在outter这个函数作用域内出现的变量时，就是闭包
def outter():
    #value1='E value stored in enclosure'#Values store in Enclosure
    def inner():
        #value1='L value stored in locals'
        # Can't find value1 in local
        print(value1, ' referenced from outter')  # 此时的value1是inner1这个函数外层函数的变量
    return inner

outter()()
