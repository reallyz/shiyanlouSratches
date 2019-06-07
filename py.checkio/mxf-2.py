'''
def got_odds():
    n=1
    while True:
        n=n+2
        yield n

def undivisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=got_odds()
    while True:
        n=next(it)
        it=filter(undivisible(n),it)

for n in primes():
    if n<10:
        print(n)
    else:
        break
#useless
'''
output=filter(lambda x:str(x)==str(x)[::-1],range(1,1000))
print(list(output))
