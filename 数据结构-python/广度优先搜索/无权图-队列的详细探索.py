
# 二维数据存储定点的关系
# 队列存储顶点
#
import  queue,random
n=5
q=queue.Queue(n)
print('入队')
for i in range(n):
    d=random.randint(0,100)
    print(d)
    q.put(d)
print('出队')
while q.empty()==False:
    print(q.get())
# 在python中，queue标准库不仅能实现队列(FIFO)
# 还能实现栈(LIFO)
# 还能实现优先级队列

# 用queue实现队列
print('queue实现栈')
def TestStack(n):
    s=queue.LifoQueue(n)
    print('入栈')
    for i in range(n):
        d=random.randint(0,100)
        s.put(d)
        print(d)
    print('出栈')
    while s.empty()==False:
        print(s.get())

TestStack(n)

# 优先级队列的实现
def PriorityQueue(n):
    '对元素值越小，优先级越高，越先出'
    p=queue.PriorityQueue(n)
    for i in range(n):
        d=random.randint(0,100)
        p.put(d)
        print(d)
    print('优先级队列出队')
    while p.empty()==False:
        print(p.get())

PriorityQueue(n)