import time

#一言蔽之：单线程是线性(同步）执行

def fun1():
    print('fun1 start time:',time.ctime())
    time.sleep(4)
    print('fun1 finish time:',time.ctime())


def fun2():
    print('fun2 start time:',time.ctime())
    time.sleep(1)
    print('fun2 finish time:',time.ctime())

def main():
    fun1()
    fun2()

if __name__ == '__main__':
    main()