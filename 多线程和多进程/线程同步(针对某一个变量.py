from atexit import register
from time import ctime,sleep
from threading import Thread,Lock,currentThread
import random
'''
线程间的同步，针对某个共同使用的变量，避免出现脏数据
需要引入更细腻的锁，锁作用在某个变量上，而不是阻塞主线程
线程锁：锁住某一段代码(某个瞬间）
1.创建全局锁对象
2.获取锁
3.释放锁
'''
#这个例子举得不好
#lock=Lock()
'''
def fun():
    #lock.acquire()
    for i in range(5):
        print('Thread-name:',currentThread().name,'i:',i,end='\n')
        #sleep(random.randint(1,5))
    #lock.release()

def main():
    t=[]
    for i in range(3):
        t.append(Thread(target=fun))
    for item in t:
        item.start()
        item.join()
if __name__ == '__main__':
    main()

'''
#把那个银行存款的改一改：
import threading

lock=threading.Lock()
balance=0
def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n

change_it(5)
print("only one thread:",balance)

def run_thread(m,n):
    for i in range(m):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1=threading.Thread(target=run_thread,args=(1000000,2,))
t2=threading.Thread(target=run_thread,args=(1200000,-1))
t1.start()
t2.start()
t1.join()
t2.join()
#balance数据不对，具有偶现性
print("two thread with enumrous times：",balance)