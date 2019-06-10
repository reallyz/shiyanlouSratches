
#为类的实例增加一些特殊的方法,关键字：实例！！！
class Student():
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return "student object (name:%s)"%self.name #print()返回的值
    __repr__=__str__                                #str返回用户看到的字符串，repr返回程序开发者的字符串
    def __len__(self):
        return 'I don\'t know how long I am'       #拥有len方法len()or __len()__

s1=Student('Tom')
print(s1,s1.__len__())

class Fib():                                       #实现for..in 循环：有__iter__()方法，__next__()直到stopIteration
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100:
            raise StopIteration()
        return self.a

for  i in Fib():
    print(i)

class subFib():                                             #__getitem__实现下标取数类似于list[i]
    def __getitem__(self, item):                            #切片对象
        if isinstance(item,int):
            a,b=1,1
            for x in range(item):
                a,b=b,a+b
            return a
        if isinstance(item,slice):
            start=item.start
            step=item.step
            stop=item.stop
            if start is None:
                start=0                                      #start,step,stop,负数都需要处理
            L=[]
            a,b=1,1
            for x in range(stop):
                if x>start:
                    L.append(a)
                a,b=b,a+b
            return L

print(subFib()[3:10])

class nonattr():                                            #__getattr__()动态增加属性
    def __init__(self,name):
        self.name=name
    def __getattr__(self, item):
        if item=='score':
            return 99                                       #也可以返回函数，函数的执行
        else:
            raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)
#print(nonattr('Tom').tom)                                  #希望跳过错误，继续执行，应该怎么操作

#实际的应用：链式调用

class Chain():
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path,item))
    '''
    def __call__(self, name):
        return Chain('%s/%s' % (self._path,name))
    '''
    def __str__(self):
        return self._path

    __repr__=__str__
#print(Chain().status.user.timeline.list)
#print(Chain().Chain('michael').repos)
#一个改进：一些REST API 会把参数放到URL中 如 GET /users/:user/repos,需要把:user替换为实际用户名
#希望 有 Chain().users('name').repos
#TODO
#Chain is not callable
class urls(Chain):
    def __init__(self,path=''):
        self._path=path
    def __call__(self, *args, **kwargs):
        return urls(('%s/%s' % (self._path, args)))
    def __len__(self):
        return 'guess what?!'
f=urls()
print(isinstance(urls().urls,urls))
print(isinstance(urls().urls,Chain)) #urls类没有__getattr__方法，去调用Chain的__getattr__方法，类就改变了
print(urls().urls('Tom').repos)


class insmethod():                                          #__call__直接在实例本身调用方法，而不是instance.method()
    def __init__(self):
        self.name='Tom'
    def __call__(self, *args, **kwargs):
        print('I am not Tom! %s'%self.name)
    def run(self):
        print('i am running!')

s=insmethod()
