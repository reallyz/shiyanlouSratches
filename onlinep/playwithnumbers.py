
from math  import modf
def splitn(n):
    t=n
    print(t,type(t))
    a=[]
    while t!=0:
        a.append(int(modf(t/10)[0]*10))
        print(a)
        b=modf(t/10)[1]
        t=b
    return a.reverse()

splitn(220)