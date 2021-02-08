
#前提是python中一切皆对象
#class是type的实例

def myfun2():
    print('I am funciton2')

def myfun3(*a):
    print(sum(a))

def outerflaw(func,text):
    def inner(*args,**kwargs):
        print('这里执行func本身的功能')
        print('在inner里面执行函数本身的功能？')
        print('以及附加的功能')
        print(text)
        return func(*args,**kwargs)
    return inner

@outerflaw(myfun2,'texy')
def myfun3(*a):
    print(sum(a))

