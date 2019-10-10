

#面向对象，类和对象
#数据成员：类变量，实例变量
#方法成员：类方法，实例方法


#具体例子
#设计一个学生类，
# 1 学生总人数，姓名，已毕业的数量
# 2 考试功能，》60 pass, not fail

class Student():
    __student_total=0
    student_graduated=0
    student__namelist=[]
    student_graduated_namelist=[]

    def __init__(self,name,age,gender):
        #实例可以动态绑定属性
        self.name=name
        self.age=age
        self.gender=gender
        self.__score=0 #其实pyhton解释器会把变量改写成_Student__score
        self.times=0
        Student.__student_total+=1
        Student.student__namelist.append(name)
    @property
    def gage(self):
        return self.age
    @gage.setter
    def gage(self,newage):
        self.age=newage
    def exam(self,examscore):
        if self.times==8:
            return 'Congratulations'
        if examscore<60:
            print('sorry,bad luck')
        elif examscore>100:
            print('get out!')
        else:
            self.__score+=examscore
            self.times+=1

            if self.times==8 and self.__score/self.times>80:
                Student.student_graduated+=1
                Student.student_graduated_namelist.append(self.name)

    def check(self,):
        if self.times<8:
            return f'you need to do more{8-self.times} tests'
        elif self.__score/self.times<80:
            return f'sorry you haven\'t meet the line,your mean score is{self.__score/self.times}'
        else:
            return 'congratulations'
    #使用方法修改变量，可以避免无效参数的传入
    @classmethod
    def get_graducated_student(cls,):
        return  Student.student_graduated

    @classmethod
    def get_gra_stulist(cls,):
        return Student.student_graduated_namelist
    @classmethod
    def get_nstu(cls,):
        return Student.__student_total


N1=Student('dd',23,'f')
N2=Student('ff',24,'m')
N1.exam(85)
N1.gage=24
print(N1.check(),N1.gage)

print(Student.get_nstu())
Student.__student_total=4 #类的属性没有被私有化，所以可以随意修改,私有化后，这就相当于绑定了一个新的属性
print(Student.__student_total is Student.get_nstu())
print(Student.get_nstu())
print(Student.__student_total)
print(globals())
print(locals())
