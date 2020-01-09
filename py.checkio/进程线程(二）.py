import os
from multiprocessing import Process
import time
def p_1(name):
    time.sleep(2)
    print('%s is running %s '%(name,os.getpid()))
def hello_world():
    time.sleep(3)
    print('%s is running and my father is %s'%(os.getpid(),os.getppid()))

if __name__=='__main__':
    print('Parent process number is %s'%(os.getpid()))
    p1=Process(target=p_1,args=('test',))
    p2=Process(target=hello_world)
    '''
    #不指定target什么都不会执行(python文档)
    p1=Process()
    p1.run=p_1 #手动重写run方法
    p1.start() #启动进程
    '''
    p1.start()
    p2.start()
    p1.join()  #join会阻塞主进程，直到子进程执行完毕。同时这也证明了python不是解释一句执行一句，而是作为整体编译后再执行
              #不然，join就不会起作用了
    p2.join()
    print('Process ends')