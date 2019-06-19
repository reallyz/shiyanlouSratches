
#多任务几乎是必然存在的
#linux fork()创建子进程，fork()调用一次，返回两次，返回子进程的ID,子进程永远返回0
import os
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
'''
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
Process (876) start...                              父子程序直接的关系可以看作链表，可以写成二叉树
I (876) just created a child process (877).         证明是返回两次，且第一次是返回子进程的pid
I am child process (877) and my parent is 876.        第二次返回的是0
                                                    注意！！！fork()并不保证程序执行的顺序，有可能是子程序先执行，还有子程序循环中也可以是父程序
for i in range(5):                                                   所以要从一个父程序fork()出多个子程序，应该再pid==0是直接break 跳出循环
    pid=os.fork()
    if pid==0:
        break
    else:
'''
#跨平台的多进程
from multiprocessing import Process #用Proce类来代表一个进程对象，多一个进程多创建一个对象

def sub_runproes(name):
    print('Run child process%s %s'%(name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s'%os.getpid())
    p=Process(target=sub_runproes,args=('test',))       #这里的test是sub_runproes的实参
    print('Child process will start')
    p.start()
    p.join()                        #join方法可以等等子进程结合后再继续往下运行，通常用于进程间的同步
    print('Child process end')

#启动大量的子进程，用进程池的方式批量创建
from multiprocessing import Pool
import time,random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)                 #pool默认的进程数是电脑核数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
'''代码结果：Parent process 669.
Waiting for all subprocesses done...
Run task 0 (671)...
Run task 1 (672)...
Run task 2 (673)...
Run task 3 (674)...
Task 2 runs 0.14 seconds.
Run task 4 (673)...
Task 1 runs 0.27 seconds.
Task 3 runs 0.86 seconds.
Task 0 runs 1.41 seconds.
Task 4 runs 1.91 seconds.
All subprocesses done.'''
#python脚本控制子程序（外部进程？？）的输入输出
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)                              #输出
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)#输入
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))                       #这里的编码有问题
print('Exit code:', p.returncode)

#进程间的通信：queue,pipes
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)                        #put
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)             #get
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

#多线程
#_thread(低级模块），threading,对_thread进行封装
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
import threading
def loop():
    print('thread %s is running!'%threading.current_thread().name)
    n=0
    while n<5:
        n+=1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(2)
    print('thread %s ended'%threading.current_thread().name)


print('threading %s is running'%threading.current_thread().name) #任何进程默认就会启动一个线程，我们把该线程称为主线程(MainThread)
t = threading.Thread(target=loop,name='Loopthread')              #函数实例化
t.start()                                                        #线程开始
t.join()
print('thread %s ended'%threading.current_thread().name)
#一个问题，线程之间共享数据，会引起影读和脏读，解决方法：上锁
#局部变量混乱
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)


def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
#问题：实际上是单线程模式，而且可以存在多个锁，不同线程
#试图获取对方的锁时可能造成死锁，导致既不执行也无法结束，只能考操作系统强制终止

#针对python,按理说，多核多线程是可以实现的
#但是有GIL锁的存在，多线程只能交替执行
#任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁
#所以python环境下，只有用多进程，每个进程有各自独立的GIL锁


#这里时针对一个线程的局部变量在调用函数时传递更简便
# 创建全局ThreadLocal对象:一个线程使用自己的局部变量作函数调用时，传递起来很麻烦
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.zzz      #局部变量之间的传递
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.zzz = name     #对象动态添加属性，同一个线程内
    process_student()           #调用了process_student 函数


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')#这是一个线程
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')  #这是另一个线程，每个线程处理的student不一样
t1.start()
t2.start()
t1.join()
t2.join()
print(process_thread('ali'))