
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,b,a,c)
        move(1,a,c,b)
        move(n-1,b,a,c)

move(3,'a','b','c')

def trim(s):
    return s.split()[0]

print(trim('  hello,world   '))

def fmm(L:str):
    if L:
        return (max(L),min(L))
    else:
        return (None,None)
print(fmm([7]))

L1= ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str)]
print(L2)

#gnerator
g=(x for x in range(10))
print(next(g),next(g))

def o():
    print('step 1')
    yield(1)
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

#does'not work
next(o())
next(o())
next(o())

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

f=fib(6)
while True:
    try:
        print("genertor：",next(f))
    except StopIteration as e:
        print("return value is :",e.value)
        break


def triangles():
    p=[1]
    while True:
        yield p
        p=[1]+[p[i]+p[i+1] for i in range(len(p)-1)]+[1]


tri=triangles()
print(next(tri))

def stinput(name):
    name=name[0].upper()+name[1:].lower()
    return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(stinput, L1))
print(L2)
from functools import  reduce
import itertools
def prod(l):
    return reduce(lambda x,y:x*y,l)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))



