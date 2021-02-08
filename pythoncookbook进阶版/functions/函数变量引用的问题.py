
'''
引用的问题：
	Python 里面传的都是引用
	初始化完成之后，就是引用当前的内存空间了。
	初始化的具体表现就是新建，赋值；
	P+=[1],这个不算是初始化，是对P所在内存空间的引用
'''

#没有初始化的两个情况：
myls=['ok']
def changls(myls):
    myls.append([1,2,3])
    print('myls inside funciont:',myls)
changls(myls)
print('myls outside function:',myls)

dictls=[]
for i in range(1,4):
    dictls.append({'num':i,'squart':i**2})
print(dictls)
#初始化完成之后的两个情况：
myls2=['not ok']
def changls2(myls):
    myls2=[]
    myls2.append([1,2,3])
    print('myls2 inside function:',myls2)
changls2(myls2)
print('myls2 outside function:',myls2)

dictls2=[]
d={}
for i in range(1,4):
    d['num']=i
    d['squart']=i**2
    dictls2.append(d)
print(dictls2)

#一个应用：定义家族谱字典，key是人名，vaule是父母，输入人名，找出所有先祖

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
                'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
             'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
            'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
            'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }
#思路：输入人名后-->父母名-->把自己去掉后，遍历字典
