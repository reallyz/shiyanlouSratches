
#存数据引用的数据结构
from typing import List, Any
import copy

def all_the_same(elements: List[Any]) -> bool:
    a = len(elements)
    f = copy.deepcopy(elements)
    if a==1:
        return True
    elif a % 2 == 0:
        elements.reverse()
        if f == elements:
            return True
        else:
            return False
    else:
        f.append(f[-1])
        elements.append(elements[-1])
        elements.reverse()
        if f == elements:
            return True

        else:
            return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([2,2,2,2]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
