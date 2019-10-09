

def trail(*p,**d):
    print(f'positional paras:{p}\n')
    print(f'keyword paras:{d}\n')
    for item,v in enumerate(d):
        print(item,v,end='')

print('\n')
print('*'*15)
#trail(1,2,3,p=1,p1=2,p3=3)
ls1=[x for x in range(10)]
ls2=[i for i in range(10,21)]
# 高阶函数
# 1.map,返回的是一个对象
mapout=list(map(lambda x,y:x-y,ls1,ls2))
print(mapout)
# 2.reduce,返回一个值
from functools import reduce
reduout=reduce(lambda x,y:x-y,ls1)
print(reduout)
# 3.filter,筛选,根据函数返回值的true or false
filout=filter(lambda x:True if x>5 else False,ls1) #三元表达式子
# 4.sorted ,排序，可以接受一个fun作为排序标准
sortout=sorted(ls1,key=abs)
print(sortout)
#装饰器，不改变原有函数的基础上增加新的功能，和偏函数作对比，/
#偏函数不增加新功能，只固定某些参数

def fun1():
    print('this is function one')

import datetime
def outter(fun):
    print('I am a decorator')
    print(datetime.datetime.today())
    return fun
#接受一个函数，返回一个函数
outter(fun1)()

@outter
def fun2():
    print('this is function two')

fun2()
#没有wrapper，添加的新功能，只要调用outter都会执行
#wrapper做隔离，但是，执行后函数名会变成wrapper
import functools
def outer_fun(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kw):
        print('I am a smarter decorator')
        print(f'the function I decorated is {fun.__name__}')
        print(datetime.datetime.today())
        return fun(*args,**kw)
    return wrapper

@outer_fun
def fun3():
    print('this is function three')

fun3()
print(fun3.__name__)
def get_para(text):
    def decorated(fun):
        @functools.wraps(fun)
        def warpped(*args,**kwargs):
            print('I am a decorator who accept para')
            print(f'my para is {text}')
            return fun(*args,**kwargs)
        return warpped
    return decorated

@get_para('hello world!')
def fun1():
    print('this is function one')

fun1()
print(fun1.__name__)