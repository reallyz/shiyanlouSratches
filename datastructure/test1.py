import math
def printStar(n:int,shape:str):
    #n=int(input('please enter the num:\n'))
    #shape=input('please enter the shape:\n')
    #n=17
    #shape='*'
    row=int(math.sqrt((n+1)/2))
    rowstar=2*row-1
    for i in range(row,-row-1,-1):
        if i==0 or i==-1:
            continue
        print((shape * (2 * abs(i) - 1)).center(rowstar, ' '))
    return n-(2*row**2-1)
if __name__ == '__main__':
    printStar(17,'*')