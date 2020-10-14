import sqlite3
from faker import Faker

conn=sqlite3.connect(':memory:')
c=conn.cursor()#游标，执行SQL语句
c.execute('create table user (id varchar(20) primary key, name varchar(20))')
fake=Faker('zh_cn')
for i in range(10):
    c.execute("insert into user (id,name) values ('{}','{}')".format(i,fake.name()))

c.execute('select * from user')
r=c.fetchall()
print(r)
#no-sql,链接到数据库，执行操作