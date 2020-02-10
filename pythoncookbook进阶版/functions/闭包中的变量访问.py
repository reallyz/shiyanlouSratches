def sample():
    n=0
    def func():
        print('n=',n)
    def get_n():
        return n
    def set_n(value):
        nonlocal n
        n=value
    #把get_n和set_n看作func的属性
    #类似于类的实例绑定属性和方法
    func.get_n=get_n
    func.set_n=set_n
    return func

f=sample()
f()
f.set_n(10)
f()
f.get_n()
#闭包模拟类的实例
import sys
class ClouserInstance:
    def __init__(self,locals=None):
        if locals is None:
            locals=sys._getframe(1).f_locals
        self.__dict__.update((key,value) for key,value in locals.items()
                             if callable(value))

def stack():
    items=[]
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    '''
    def __len__():
        return len(items)
    '''
    return ClouserInstance()


s=stack()
s.push(10)
s.push('how')
s.pop()
