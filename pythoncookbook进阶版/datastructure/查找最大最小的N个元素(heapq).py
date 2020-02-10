
#怎样从一个集合中获得最大或者最小的 N 个元素列表？
#如果你想在一个集合中查找最小或最大的 N 个元素，并且 N 小于集合元素数量，
#那么这些函数提供了很好的性能。 因为在底层实现里面，首先会先将集合数据进行堆排序后放入一个列表中
import heapq
import random
random.seed(10)
nums=[random.randrange(1,100) for x in range(10)]
print('the smallest three:\n',heapq.nsmallest(3,nums))
print('the largest three:',heapq.nlargest(3,nums))
# 这两个函数都接受关键字参数
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(3,portfolio,key=lambda s:s['shares']))

