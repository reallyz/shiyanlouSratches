
#包含N个元素的!可迭代对象!同时赋值给m个变量

# 1 n=m
ls=[1,2,3,4]
a,b,c,d=ls
s='hello'
a,b,c,d,e=s
# n>m
# 使用占位符号 _ ,使用*
a,_,c,d=ls
a,*b=s

# *号表达在迭代元素为可变长的序列时很有用
lss=[[1,2],[1,2,3],[1,2,3,4]]
for i,*j in lss:
    print(i,*j)

# *，_联合使用，解压然后丢弃,最好用ign(ignore)来命名要丢弃的变量

a,*ign,b=lss
print(ign)
del ign
print(ign)
