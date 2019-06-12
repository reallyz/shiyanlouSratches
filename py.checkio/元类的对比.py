#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student():
    name='student'
    def __init__(self):
        self.name='I'
        self.age=4
    def show(self):
        print('my name is{},I am {} years old,my height is {}'.format(self.name,self.age,self.height))

lihua=Student()
lihua.height=180 #这么写不合适
Student.height=180 #这么写更不合适，这是类的属性
#以上为动态的绑定实例和类的属性
del Student.height

lihua.show()

def run(self):
    print('a normal person can run 10 miles per hour')

#lihua.run=run
Student.run=run
lihua.run()
#不能直接给实例添加方法
#可直接给类添加方法

#使用类对象添加类方法
@classmethod
def play_game(cls):
    print('I love playing games')

Student.play_game=play_game
lihua.play_game()
#使用类对象添加静态方法
@staticmethod
def study():
    print('study makes me happy!')

Student.study=study
lihua.study()
#使用type继承，并添加方法

def sleep(self):
    print('I don\'t wanna leave my bed')
Student=type('Student',(Student,),dict(sleep=sleep))

#type 相当于创建了一个新的类，lihua不是从这个新建类实例化来的，所以没有sleep方法
liming=Student()
liming.sleep()
lihua.sleep() #AttributeError: 'Student' object has no attribute 'sleep'

#元类：批量化创建类的方法