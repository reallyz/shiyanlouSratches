import time
def PrintInfo():
    print('hello!this is for competition predict\n')
    print('please enter prob of A,B, and the n\n')
    print('please wait with patient')
def GetInput():
    n=input()
    pa,pb,n=eval(n)
    return pa,pb,n
def PrintSumm(wa,n):
    print('A wins {} times,rate{:.1%},'
          'B wins {} times,rate{:.1%}'.format(wa,wa/n,n-wa,(n-wa)/n))

def OneGame(pa,pb):
    sa,sb=0,0
    wa=0
    from random import random
    for i in range(5):
        home={pa,pb}.pop
        #home=pa
        n, s = 0, 0
        while (n<15)and(s<15):
            if home==pa and home>random():
                n+=1
            else:
                home=pb
                if home>random():
                    s+=1
                else:
                    home=pa

        #time.sleep(1)
        if n>s:
            sa+=1
        else:
            sb+=1

    if sa>sb:
        return wa+1

def simNgmes(n,pa,pb):
    s=0
    while n:
        wa=OneGame(pa,pb)
        if wa:
            s=s+wa
        n=n-1
    return s

def main():
    PrintInfo()
    pa,pb,n=0.45,0.5,1000
    wa=simNgmes(n,pa,pb)
    PrintSumm(wa,n)

if __name__=='__main__':
    for i in range(10):
        main()


