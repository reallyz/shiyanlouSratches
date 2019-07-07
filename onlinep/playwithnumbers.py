
from math  import modf
def splitn(n:int,k=2):
    t=n
    times=k*n
    #print(t,type(t))
    a=[]
    c=[]
    while t!=0:
        a.append(round(modf(t/10)[0]*10))
        #print(a)
        b=modf(t/10)[1]
        t=b
    a.sort()
    while times!=0:
        c.append(round(modf(times / 10)[0] * 10))
        #print(c)
        d = modf(times/10)[1]
        times = d
    c.sort()
    if a==c:
        #return print('Yes!The number is:\n',n*k)
        return True
    '''
    else:
        return print('No!')

    '''
#find the number under 123456789+1:

for x in range(123456789+1):
    a=[]
    if splitn(x):
        print(x)
        a.append(x)
