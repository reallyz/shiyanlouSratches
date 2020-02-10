

#假定你要从一个记录（比如文件或其他类似格式）中的某些固定位置提取字段

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
#20：23，31：37是硬编码，可读性差
# solution：使用切片对象
shares=slice(20,23)
price=slice(31,37)
cost=int(record[shares])*float(record[price])
#任何使用切片的地方都可以使用切片对象
#del record[shares]
#record[shares]='123'
#使用 indices(size),这样不会产生indexerror异常,只是将边界的值缩小，并不是成比例缩小
s='helloworld'
a=slice(12,20,2)
print(type(a.indices(len(s))),a.indices(len(s)),len(s))
for i in range(*a.indices(len(s))):
    print(s[i])
