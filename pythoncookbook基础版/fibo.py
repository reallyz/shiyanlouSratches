def  fib(n):
    # print fib up to n
    a,b=0,1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b
    print()


def fib2(n):
    a,b=0,1
    ls=[]
    while b<n:
        ls.append(b)
        a,b=b,a+b
    return  ls

vinm=10
