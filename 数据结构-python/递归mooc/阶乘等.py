

def factoria(n):
    if n<0:
        print('please enter a positive integer')
    if n==0:
        return 1
    else:
        return n*factoria(n-1)
#关键在于n
print(factoria(5))
i=0
def hano(n,a,b,c):
    global i
    if n<0:
        print('please enter a positive integer')
    if n==1:
        i+=1
        print(f'{i}:{a}-->{c}')
    else:
        hano(n-1,a,c,b)
        hano(1,a,b,c)
        hano(n-1,b,a,c)
a='a'
b='b'
c='c'
hano(2,a,b,c)
#关键在于交换a,b,c的地位
#每次调用都是一个新的函数，所以i是全局变量
#不一定要再return里调用自己，递归：有递推关系，有出口条件
def draw_line(length,label=''):
    line='-'*length
    if label!='':
        line+=''+label
    print(line)
def draw_interval(length):
    if length>0:
        draw_interval(length-1)
        draw_line(length)
        draw_interval(length-1)
def draw_ruler(num,length):
    draw_line(length,'0')
    for j in range(1,1+num):
        draw_interval(length-1)
        draw_line(length,str(j))


num=4
length=6
draw_ruler(num,length)
#逻辑上的清晰处理
#标刻度和划线分离