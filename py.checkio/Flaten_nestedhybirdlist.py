def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el,(str,bytes)):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

def flat_list(l):
    for x in l:
        if hasattr(x,'__iter__') and not isinstance(x,(str,bytes)):
            yield from  flat_list(x)
        else:
            yield x

print(flatten([1,2,3,[12,33]]))