
#函数，先从函数参数说起，分为位置参数(xx)，和关键字参数(xx=xx)#
#加星号可变
#%%
def test(first,*bb,verylast=4):
    return (first+sum(bb))/(1+len(bb))
#%%
print(test(6,12,3,4,56,verylast=6))

def test1(first,*b,last):#强制关键字参数
    print(f'hi,i am{first},{b},{last}')
test1(12,32,4,2,41,last=4)
def test2(*args,**kwargs):
    print(f'hi i am from {args}')
    print(f'hi i am from {kwargs}')
test2(1,2,3,4,w=1,b=2,c=3)
#匿名函数
names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']
#按照名来排
print(sorted(names,key=lambda name:name.split()[-1].lower()))
#匿名函数捕获变量
x=10
a=lambda y:x+y
x=20
b=lambda y:x+y
a(10)==b(10)
#此时，匿名函数的变量运行的时候才确定
#如果想实现默认参数的效果：
x=30
aa=lambda y,x=x:x+y
#应用
f=[lambda x,n=n:x+n for n in range(5)]
for fs in f:
    print(fs(4))
