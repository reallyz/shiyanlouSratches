
# 找出列表中的缺失值
def findm(ls):
    sta=ls[0]
    for i in range(len(ls)):
        if sta!=ls[i]:
            print(f'the missing n is {sta}')
            break
        sta+=1

ls=[2,3,4,6,7,8]
findm(ls)



#设计一个人员类，姓名，年龄，性别
class Person():


    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class Teacher(Person):

    def __init__(self,name,age,gender,title,degree,years,salary):
        # __init__是个魔法函数,不用.init显式地调用
        super().__init__(name,age,gender)#超类，找不到的属性去父类中找
        self.title=title
        self.degree=degree
        self.years=years
        self.salary=salary


    def CountTotalSalary(self,):
        return self.salary+self.years*100


ZX=Teacher('zs',34,'m','Pro','Phd',20,20000)
print(ZX.CountTotalSalary(),ZX.name)

class A():
    def __init__(self,color,shape):
        self.color=color
        self.shape=shape

class a(A):
    def run(self,):
        print('I am run')

aa=a('red','square')
aa.run()
print(aa.shape,aa.color)
#超类

print('*'*12)
class B():
    def __init__(self):
        print('enter B')
        print('leave B')
b=B()
print('*'*12)
class C(B):
    def __init__(self):
        print('enter c')
        super().__init__()
        print('leave C')

c=C()
print('*'*12)
class D(B):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')

d=D()
print('*'*12)


class E(C,D):
    def __init__(self,):
        print('enter E')
        super().__init__()
        print('leave E')


e=E()
print('*'*12)
