def cC():
    fs=[]
    def m(i):
        def f():
            return i*i
        return f
    for i in range(1,4):
        fs.append(m(i))
    return fs

#一个错误
'''
def is_old(n):
    return lambda:n,n%2==1
l=list(filter(is_old,range(1,21)))
l
Out[70]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
is_old(5)
Out[80]: (<function __main__.is_old.<locals>.<lambda>()>, True) ！！！lambda函数会直接执行，而filter需要的时函数的引用,而不是函数的执行
def ww(c):
    return c%2==1
l=list(filter(ww,range(1,12)))
l
Out[86]: [1, 3, 5, 7, 9, 11]
ww(12)
Out[87]: False
'''
#闭包：内部函数使用了外部函数的临时变量，外部函数返回内部函数的引用