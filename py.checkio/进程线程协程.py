
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
Process (876) start...
I (876) just created a child process (877).         证明是返回两次，且第一次是返回子进程的pid
I am child process (877) and my parent is 876.        第二次返回的是0

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
