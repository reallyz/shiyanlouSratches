

#局部变量和全局变量
#局部变量为组合数据类型（就是里面什么类型都可以放），
#且未创建，等同于全局变量
ls=['F','f']#全局变量
def funls(a):
    ls.append(a)  #没有改指针
    return
funls('c') #全局变量被修改

def funs(a):
    ls=[]    #已经创建，有了新的指针?
    ls.append(a)
    return

n,s=1,5
def p(o):
    global s
    s=s+o
    print(o+s)
    return
p(10)

