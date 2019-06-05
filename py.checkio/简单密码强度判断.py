
def checkio(data: str) -> bool:
    if len(data)<10:
        print('data<10,retry')
        return False
    else:
        n=0
        m=0
        l=0
        for i in data:
            if  i.islower():
                n=n+1
            elif i.isdigit():
                m=m+1
            elif i.isupper():
                l=l+1
        print(n, m, l)
        if m*n*l!=0:

            return True
        else:
            return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
