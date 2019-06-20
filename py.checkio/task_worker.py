import random,time,sys
from multiprocessing.managers import BaseManager

class queManager(BaseManager):
    pass


#worker里的queue只从网络上获取，所以注册时只提供名字
queManager.register('get_task_que')
queManager.register('get_result_que')
#连接到服务器，也就是运行task_master.py的机器
server_addr='127.0.0.1'
print('connect to server %s'%server_addr)
#端口和验证码注意和task_master.py保持一致
m=queManager(address=(server_addr,5000),authkey=b'abc')
#从网络连接
m.connect()
#获取queue的对象：
task=m.get_task_que()
result=m.get_result_que()
#从task队列写任务，并把结果写入result队列
while not task.empty():
    n=task.get(timeout=1)               #这里是等待时间
    print('run task %d * %d..'%(n,n))
    r='%d*%d=%d'%(n,n,n*n)
    time.sleep(2)
    result.put(r)
print('task queue is empty.')
print('worker exit.')

if __name__=='__main__':
    pass

