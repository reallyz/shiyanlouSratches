

# 赋值
a=5
b=7
print(a,b,end='\n')
a,b=b,a
print(a,b,end='\n')
a,b,c=1,2,3
print(a,b,c,end='\n')
#unpack
ls=[9,7,4,2]
a,b,c,d=ls
print(a,b,c,d,end='\n')
#*号收集
a,*b,c=ls
print(a,b,c,end='\n')
# *号展开，针对序列
s='how are you'
print(*s,'\n')
# *号展开，针对字典
d={'a':1,'b':2,'c':3}
print([*d],'\n',{**d,'d':4},'\n')
# ，号放最后的解包
ll=[[12,2,3]]
b,=ll
print(b)
