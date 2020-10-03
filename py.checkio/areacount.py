import numpy as np

#这个版本的方向错了
'''
思路是，加法思路，如果#在行中，就加一行，然后题目要求的是，如果全零行在中间，也要算进面积
于是设置了判定在中间的条件，但是还有另一种情况，就是首行是全零后，中间行也是全零就失效了比如64行的那种情况
'''
def house(plan):
    # outtemp=plan.splitlines()
    outtemp = plan.strip('\n').split('\n')
    out = [list(x) for x in outtemp]
    temparr = np.array(out)
    row, col = temparr.shape
    height = 0
    width = 0
    for j in range(row):
        tmprow = temparr[j, :]
        if '#' in tmprow:
            width += 1
        if j != 0 and j != row - 1:
            if '#' not in tmprow:
                width += 1

    for i in range(col):
        tmpcol = temparr[:, i]
        if '#' in tmpcol:
            height += 1

        if i != 0 and i != col - 1:
            if '#' not in tmpcol:
                height += 1

    area = width * height

    return area


if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
