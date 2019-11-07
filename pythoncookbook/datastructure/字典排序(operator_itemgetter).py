
#排序都是针对一个数据单元排序，比如
# 对列表排序，是对列表元素排序，而这个列表元素可能是：字典，元组，字符串，元组，集合等


#字典的最大最小值
#字典结构
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
#按价格排序，返回价格对应的key
print(max(prices,key=lambda k:prices[k]))
#按key的字母顺序排序，返回key
print(max(prices))
#按价格排序，返回元组
print(max(zip(prices.values(),prices.keys())))
#列表结构
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
print(max(rows,key=lambda d:d['fname']))

#排序
from operator import itemgetter
rows_by_lname=sorted(rows,key=itemgetter('lname'))
rows_by_uid=sorted(rows,key=itemgetter('uid'))
print(rows_by_lname)
print(rows_by_uid)
#支持多个keys
rows_by_lu=sorted(rows_by_uid,key=itemgetter('lname','uid'))
#排序类型相同的对象，但不支持原生的比较

class User:
    def __int__(self,user_id):
        self.user_id=user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

