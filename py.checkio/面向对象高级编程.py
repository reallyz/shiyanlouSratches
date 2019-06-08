


'''使用__slots__限制实例的属性'''
'''使用@property,把方法变成属性只读，@函数名.setter可写,有setter必须有property'''
class Stundet():
    #__slots__ = ('name','gender','score')

    def __init__(self,name,gender,_score):
        self.name=name
        self.gender=gender
        self._score=_score

    @property
    def get_score(self):
        return self._score
    def set_score(self,vaule):
        if not isinstance(vaule,int):
            raise ValueError('must be an integer')
        if vaule<0 or vaule>100:
            raise ValueError('out of range')
        self._score=vaule
    @property
    def birth(self):
        return self._birth      #初始化属性
    @birth.setter
    def birth(self,value):
        self._birth=value       #设置属性
    @property
    def age(self):
        return 2019-self._birth
Tom=Stundet(name='Tom',gender='M',_score=110)
print(hasattr(Tom,'name'))
print(Tom.get_score)
Tom.birth=1988#可赋值
print(Tom.birth,Tom.age)#可取值


class Screen(object):
    @property
    def shape(self):
        return self._width,self._height
    @shape.setter
    def shape(self,val):
        self._width,self._height=val
    @property
    def resolution(self):
        return self._height*self._width

s=Screen()
s.shape=(1024,768)
print('resolution=',s.resolution)

#鸭子语言
class Animal():
    def run(self):
        print('Animal is running!')

class Dog(Animal):
    def run(self):
        print('Dog is running!')

dog=Dog()
dog.run()
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)

class timer():
    def run(self):
        print('start to time')
    def stop(self):
        print('Stop!')
time=timer()
run_twice(time)
print(type(dog),isinstance(dog,(Dog,Animal)))