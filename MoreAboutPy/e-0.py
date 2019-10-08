
#三角形三边及面积判断
'''
import math
a=eval(input('pleas enter a side:'))
b=eval(input('pleas enter a side:'))
c=eval(input('pleas enter a side:'))
print(f'your a is {a},b is {b}, c is {c} \n')
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f'the area is {s}\n')
else:
    print('cannot be a tangle \n')
'''


#逆素数
ls=[]
def nisprime(n):
    flag=1
    for j in range(2,n):
        if n%j==0:
            flag=0
            break
    return flag


def reverseN(n):
    t=0
    while n!=0:
        d=n%10
        n=n//10
        t=t*10+d
    return t


for i in range(2,201):
    if nisprime(i):
        if nisprime(reverseN(i)):
            ls.append(i)

print(ls,len(ls))