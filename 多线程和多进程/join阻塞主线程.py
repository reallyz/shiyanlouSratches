import  threading
import  time

print('Main thread start')
def run():
    time.sleep(2)
    print('thread name is:',threading.currentThread().name)
    print('I am being completely executed')
if __name__ == '__main__':
    start_time=time.time()
    threadls=[]

    for i in range(5):
        threadls.append(threading.Thread(target=run))
    # 这样就是阻塞整个线程了，顺序执行了,并没有多线程同时执行
    # for t in threadls:
    #     t.start()
    #     t.join()
    for t in threadls:
        t.start()
    #阻塞主线程，主线程要等待所有子线程结束后，自身才结束
    for t in threadls:
        t.join()
    print('Main thread is done')
    print('time cost:',time.time()-start_time)