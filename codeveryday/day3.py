
'''
#fib
a= 1
b = 1
c = a + b
n=0
while n<20:
    a = b
    b = c
    c = a + b
    print(c)
    n+=1
# print c is not complete
'''


'''
#true factor
def truefactor(n):
    sum=0
    flag=0
    for i in range(1,n):#python for loop is lame
        if(n%i==0):
            sum+=i
    if(sum==n):
        flag=1
    return flag
for i in range(1,1000):
    if(truefactor(i)):
        print(i)
'''

#prime number
import  math
def findprime(n):
    m=int(math.sqrt(n))
    flag=1
    for i in range(2,m):
        if(n%i==0):
            flag=0
            break
    return flag

#print(findprime(13))
for i in range(2,101):
    if(findprime(i)):
        print(i)





