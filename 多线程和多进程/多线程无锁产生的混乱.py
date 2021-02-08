import threading
import time

balance=0
def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n

change_it(5)
print("only one thread:",balance)

def run_thread(m,n):
    for i in range(m):
        change_it(n)

t1=threading.Thread(target=run_thread,args=(1000000,2,))
t2=threading.Thread(target=run_thread,args=(1200000,-1))
t1.start()
t2.start()
t1.join()
t2.join()
#balance数据不对，具有偶现性
print("two thread with enumrous times：",balance)