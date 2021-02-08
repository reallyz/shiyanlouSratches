from multiprocessing import Process
import os
from atexit import register
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

#退出函数的装饰器用法
@register
def _btexit():
    print('done')
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    #p.join()
    #虽然主进程结束的更快，但子进程仍然能执行完毕，证明资源是独立的
    print('Child process end.')