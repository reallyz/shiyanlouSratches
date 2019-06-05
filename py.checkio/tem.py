def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    line=line.lower()
    import string
    if  line:
        jishu = 1
        t = 0
        for i in range(1,len(line)):
            if line[i] != line[i-1]:
                if t < jishu: t = jishu
                jishu = 1
            else:
                jishu = jishu + 1
        return max(t,jishu)
    else:
        return 0

from itertools import  groupby
def long_r(line):
    return max((sum(1 for _ in g) for k,g in groupby(line)),default=0)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(long_r('abcabcabcc'))

    assert long_r('sdsffffse') == 4, "First"
    assert long_r('ddvvrwwwrggg') == 3, "Second"
    assert long_r('abababaab') == 2, "Third"
    assert long_r('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
