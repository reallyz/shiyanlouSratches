
#task_master.py
#服务进程：启动 queue，把queue注册到网络，往queue里写任务
import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support


task_que=queue.Queue()              #这里没有定义task的数量，所以队列的长度是无穷大
result_que=queue.Queue()


class QueManager(BaseManager):
    pass
#注册两个que到网络上
def gettask():
    return task_que
def getresult():
    return result_que
 #windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
def test():
    QueManager.register('get_task_que',callable=gettask)
    QueManager.register('get_result_que',callable=getresult)
    # 绑定端口并设置验证码，windows下需要填写ip地址，linux下不填默认为本地
    manager=QueManager(address=('127.0.0.1',5000),authkey=b'abc')
#启动queue
    manager.start()
#获得通过网络访问的queue对象
    try:
        task=manager.get_task_que()
        result=manager.get_result_que()
    #任务实验
        print('start to put')
        for i in range(10):
            n=random.randint(0,1000)
            print('put task %d'%n)
            task.put(n)
        print('start to get result')
        print(result.full())
        #while not result.full():
            #time.sleep(1)
        for i in range(10):
            print(result.full())
            r=result.get()
            print('Result: %s'%r)
    except:
        print('manager error')
    finally:
        # 关闭
        manager.shutdown()
        print('master exit')


if __name__=='__main__':
    freeze_support()
    test()