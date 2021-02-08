

def fun1():
    print('I am fun1 from fun1')

def fun2():
    return 1+1

if __name__ == '__main__':
    fun1()
    assert fun2()==1
    