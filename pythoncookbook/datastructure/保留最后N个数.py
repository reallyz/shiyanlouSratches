
#在迭代操作中，变量的值会被覆盖，
#如何保留最后有限几个元素的记录？
from collections import deque
# deque是一个队列，但新的元素加入，并且队列已经满了的时候
# 最先入队元素就会被移除
# 带有生成器的函数
def search(lines,pattern,history=5):
    previous_lines=deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)
path=r'/root/PycharmProjects/shiyanlouSratches/新时代.txt'
# 打开一个文件对象，逐行读入
with open(path) as f:
    for line,prevlines in search(f,'中国梦',5):
        for pline in prevlines:
            print('I am here and done!')
            print(pline,end='**')
        print(line,end='****')
        print('-'*20)
