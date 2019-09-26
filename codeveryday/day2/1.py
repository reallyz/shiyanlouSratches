import random
import string

import pymysql  # 链接到关系数据库


def GenCoup(n):
    words=string.ascii_letters+string.digits
    coupon=''
    for i in range(n):
        coupon+=random.choice(words)
    return coupon

n=10
#sql语法，编写方式，程序范式(try,except,链接，提交，关闭)
try:
    conn=pymysql.connect(host='127.0.0.1',user='root',passwd='kalicode',port=3306)
    cur=conn .cursor()
    conn.select_db('lhd')
    cur.execute('drop table if exists coupon')
    sql='''create table coupon(
            id int,
            uuid varchar(50)
            )
        '''
    cur.execute(sql)
    for i in range(1,201):
        num='%03d'%i
        num+=GenCoup(n)
        cur.execute('insert into coupon values(%s,%s)',(i,num))
    conn.commit()
    cur.close()
    conn.close()
except pymysql.Error as e:
    print('mysql error {}:{}'.format(e.args[0],e.args[1]))
