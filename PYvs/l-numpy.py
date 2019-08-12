import numpy as np
from PIL import Image

#numpy,数据类型：ndarray
#读取，统计函数，梯度函数
#基本生成函数
b=np.arange(20).reshape((4,5))
np.eye(3)
np.ones((2,3))
np.zeros((2,3))
np.ones_like(b)
#维度变换
np.resize(b,(5,4))
b.reshape((2,10))
print(b.flatten())
#类型转换
#类型创建(dtype),可以预定义类型，计算更快dtype=
#example
student=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(type(student),student)
a=np.array([('Tom',12,90),('Jack',13,91)],dtype=student)
print(a,a[1])
c=b.astype(np.float)
print(c)
#索引与切片，由外层到内层
#运算，每个元素运算，np.dot(),向量内积
#存取
'''
np.savetxt
np.loadtxt #仅一维，二维
b.tofile
np.fromfile()
np.save
np.load()
'''
#随机函数，生成随机数组更方便，高级方法，排列，随机选择
d=np.random.rand(3,4)
e=np.random.poisson()
f=np.random.choice(d.flatten(),(2,3))
print(f)
#统计函数，最值，方差，均值

#梯度函数
np.gradient(d)
#图像处理，信号处理
'''
#数组与图像处理，是一大应用方向
im=np.array(Image.open('test.jpg'))
b=[255,255,255]-im  #最内层,可以看作是坐标，和对坐标的描述
imm=Image.fromarray(b.astype(np.uint8))
imm.save("testm.jpg")

print(im.shape,im.dtype)
'''