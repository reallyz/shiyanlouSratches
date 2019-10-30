import  sys
# TODO list like string can be subscripted,but can also be at left
f=[x for x in range(10)]
g=(x for x in range(10))
print(f"size of f:{1},size of g:{2}".format(sys.getsizeof(f),sys.getsizeof(g)))
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
# when data is very small,this way is more efficient
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
#print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
print(f)
'''
for val in f:
    print(val)
'''
# TODO tuple is faster than list,and in multiprocess,we need constant variant
tuple1=(1,2,3,4)
g_tuple=tuple(f)
print("size of g_tuple:",sys.getsizeof(g_tuple))

# TODO set,one and only ,cannot be subscriptable
set1={1,2,3,4}
set2=set(x for x in range(10))
set1.add(5)#scalar
set1.update([1,2,3])#can be vector
set1.remove(1) #if not exist,raise error
set1.discard(2)
set1.pop() # random delete
# operation 可以调用集合对象的方法，
# 也可以直接使用对应的运算符，例如&运算符跟intersection方法的作用就是一样的
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2)),在set1里面删除set1,set2的交集

# TODO dict is powerful,key must be hashable:string.tuple

# 创建字典的字面量语法
d1={"a":18,"b":4,'C':45}
# 创建字典的构造器语法
d2=dict(one=1, two=2, three=3, four=4,liming=34)
# 通过zip函数将两个序列压成字典
d3=dict(zip(['a','b','c'],[11,21,31]))
# 创建字典的推导式语法
d4 = {num: num ** 2 for num in range(1, 10)}
# get方法也是通过键获取对应的值但是可以设置默认值
print(d4.get('武则天', 60))
