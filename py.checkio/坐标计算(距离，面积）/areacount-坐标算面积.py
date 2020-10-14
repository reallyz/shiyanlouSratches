import numpy as np

#这个版本的方向错了
'''
思路是，加法思路，如果#在行中，就加一行，然后题目要求的是，如果全零行在中间，也要算进面积
于是设置了判定在中间的条件，但是还有另一种情况，就是首行是全零后，中间行也是全零就失效了比如64行的那种情况
但是64行的特征是0行连续
另一个方法：坐标重合围成面积来算
'''
def house(plan):
    # outtemp=plan.splitlines()
    outtemp = plan.strip('\n').split('\n')
    out = [list(x) for x in outtemp]
    temparr = np.array(out)
    vec = np.argwhere(temparr == '#')
    if vec.size==0:
        area=0
    else:
        height=vec[:,0].max()-vec[:,0].min()+1
        width=vec[:,1].max()-vec[:,1].min()+1
        area=height*width

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
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12
assert house('''
0000
0000
#000
''') == 1

print("Coding complete? Click 'Check' to earn cool rewards!")
