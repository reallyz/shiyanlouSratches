import threading
from time import sleep,ctime
'''
threading 模块的target参数不仅能接收一个函数，而且可以接收一个对象(类的实例）,这个被称为线程对象
线程对象对应的类，需要有可以传入线程函数和参数的构造方法，而且类中还必须有一个名为'__call__'的方法
（和迭代器对象需要实现__iter__,__next__方法一样）
当线程启动时，会自动调用线程对象里面的__call__方法，然后在该方法(__call__)中调用线程函数
'''

class MyThread():
    def __init__(self,func1,func2,args):
        self.func=func1
        self.funcs=func2
        self.args=args
    def __call__(self):
        self.func(*self.args)
        self.funcs(*self.args)


def fun(index,sec):
    print('start:',index,'at:',ctime())
    sleep(sec)
    print('stop:',index,'at:',ctime())

def main():
    t1=threading.Thread(target=MyThread(fun,fun,(1,3)))
    t2 = threading.Thread(target=MyThread(fun,fun, (2, 2)))
    t3 = threading.Thread(target=MyThread(fun,fun, (3, 5)))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
if __name__ == '__main__':
    main()
