#解决各个编程语言件传输和存储的问题
import json
dd={'name':'xihua','age':20,'score':90}
'''
ddj=json.dumps(dd)
rddj=json.loads(ddj)
with open('ddj.txt','w') as f:
    json.dump(dd,f)
f=open('ddj.txt','r')
json.load(f)
f.close()
'''
class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

s=Student('ximin',21,97)
print(type(s))
#json.dumps(s)         #此处会报错，dumps不知道如何处理这个类，json的默认对象就只有
'''
JSON类型	Python类型
{}	        dict
[]	        list
"string"	str
1234.56	    int或float
true/false	True/False
null	    None
'''
#但是dumps接受函数参数转换为json对象
def student2dict(s):
    return {
        'name':s.name,
        'age':s.age,
        'score':s.score
    }
json_str=json.dumps(s,default=student2dict)      #从类转换为字典
print(json_str)
#json.dumps(s,default=lambda obj:obj.__dict__))
# 通常class的实例都有一个__dict__属性，用来存储实例变量。例外：定义了__slots__的class
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
print(json.loads(json_str,object_hook=dict2student)) #从字典转为类
