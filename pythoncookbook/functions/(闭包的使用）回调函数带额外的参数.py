

def apply_async(func,args,*,callback):
    # compute the result
    result=func(*args)
    # invoke the callback function
    callback(result)


def print_result(result):
    print('Got:',result)


def add(x,y):
    return x+y

apply_async(add,('hello','world'),callback=print_result)

# 如何让回调函数携带更多的信息？

#TODO 使用类绑定方法
class ResultHandler:
    def __init__(self):
        self.sequence=0
    def handler(self,result):
        self.sequence+=1
        print(f'{[self.sequence]}Got:{result}')

r=ResultHandler()
print(type(r),type(r.handler(r)))
apply_async(add,(5,6),callback=r.handler)
apply_async(add,('how','are'),callback=r.handler)
#TODO 使用闭包捕获变量值,变量作用域的范围，全局变量任何函数都可以使用，而局部变量只能在函数定义的范围类使用
def chandler():
    sequence=0
    def print_result(result):
        nonlocal sequence
        sequence+=1
        print(f'{[sequence]}Got:{result}')
    return print_result
c=chandler()
apply_async(add,(12,13),callback=c)
apply_async(add,(13,14),callback=c)
#TODO 使用协程
def make_handler():
    sequence=0
    while True:
        result=yield
        sequence+=1
        print(f'{[sequence]}Got:{result}')
handler=make_handler()
print(dir(handler))
next(handler)
apply_async(add,(12,13),callback=handler.send)
apply_async(add,(13,14),callback=handler.send)

