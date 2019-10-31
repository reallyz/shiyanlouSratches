
#继承和多态

# TODO 通常情况下，子类的功能属性比父类多

class Person():
    def __init__(self,name,age):
        self._name=name
        self._age=age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return  self._age
    @name.setter
    def name(self,name):
        self._name=name
    def play(self):
        print("%s is playing"%self._name)
class Student(Person):
    #已经相当于对父类重写方法了
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self._grade=grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,grade):
        self._grade=grade
    def mygrade(self):
        print("your score is %d"%self._grade)

# TODO 抽象类，就是专门用来作模板的类，不能实例化，意义何在？
from abc import ABCMeta, abstractmethod
class Pet(object,metaclass=ABCMeta):
    def __init__(self,nickname,age):
        self._nickname=nickname
        self._age=age
    @abstractmethod
    def make_voice(self):
        pass
    #@abstractmethod
    #@property
    def nickename(self):
        pass
    @property
    def age(self):
        pass
class Dog(Pet):
    def make_voice(self):
        print("%s wowowo"%self._nickname)
    @property
    def age(self):
        return self._age
def main():
    p=Person('Anton',45)
    p.name='lion'
    p.play()
    s=Student('villanelle',25,91)
    s.name='eve'
    s.play()
    s.grade=92
    s.mygrade()
    d=Dog("tom",10)
    d.make_voice()
    print(d.age)
if __name__=="__main__":
   main()
