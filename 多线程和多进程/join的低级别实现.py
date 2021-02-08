import _thread as thread
from  time import ctime,sleep
'''
锁是为了，让主程序感知到线程函数的存在：
1.有线程函数在执行时不退出
2.线程函数执行完毕后立即退出
锁的使用分为三个步骤：
1.创建锁
2.获取锁
3.释放锁
'''

def fun(sec,index,loc):
    print('start',index,'time:',ctime())
    sleep(sec)
    print('finish',index,'time:',ctime())
    loc.release()

def main():
    loc1=thread.allocate_lock()
    loc1.acquire()
    thread.start_new_thread(fun,(5,'first',loc1))
    loc2 = thread.allocate_lock()
    loc2.acquire()
    thread.start_new_thread(fun, (3, 'second', loc2))
    #还是要依靠while循环来保证线程函数运行,注释掉while循环，主程序依旧无法感知
    while loc1.locked() or loc2.locked():
        pass
if __name__ == '__main__':
    main()