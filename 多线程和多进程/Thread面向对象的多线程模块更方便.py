import threading
from time import sleep,ctime
'''
把_thread面向过程的步骤，方法化，更简单
join方法可以阻塞主线程，保证线程函数执行完毕后再结束
一般步骤：
1.创建线程对象
2.启动线程
3.阻塞主线程
'''
def fun(index,sec):
    print('start:',index,'time:',ctime())
    sleep(sec)
    print('finish:',index,'time:',ctime())

def main():
    #print(ctime())
    thread1=threading.Thread(target=fun,args=('first',4))
    thread2=threading.Thread(target=fun,args=('second',2))
    #这里主线成只是负责把函数线程trigger起来了，主线程的任务已经结束了
    #如果不阻塞主线程，那么主线程执行完毕就退出，而函数线程(并不独立于主线程)又是挂载在主线程上的
    #所以很有可能函数线程还未执行就消失了
    thread1.start()

    thread2.start()
    #thread1.join()
    #thread2.join()
    #print(ctime())
if __name__ == '__main__':
    main()