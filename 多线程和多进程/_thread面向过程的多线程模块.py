from 单线程演示 import fun1,fun2
#import _thread as thread
import threading
#使用的是_thread模块中的start_new_thread 函数
#这个函数接收两个参数，一个是线程函数，一个是以元组形式的函数参数
def main():
    #开启一个新的线程
    #thread.start_new_thread(fun1,())#把单线程演示.py里的时间注释掉后，fun1直接就不执行了
    threading.Thread(target=fun1).start()#结果发现，threading模块是一定会让线程函数执行完毕的，的join方法更多强调的是线程函数的完整性
    fun2()
#这里的执行结果是只有fun2,因为主程序没有感知线程函数是否执行完毕
#很神奇，明明是一体的，但执行起来却像是分开了一样
if __name__ == '__main__':
    main()