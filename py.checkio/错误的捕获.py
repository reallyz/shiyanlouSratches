
#TODO
#错误的捕获
try:
    print('try...')
    r = 10 / 0#后面的print不会再执行
    print('result:', r)#可能有错的代码
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e) #多个错误捕获，这些错误都源自于BaseException，而且错误间取并集
else:                              #整个结构相当于 try -if(有错误）：执行的代码 -else: 执行的代码 -finally:执行的代码
    print('no error!')
finally:
    print('finally...')
print('END')
#TODO
#可以跨层调用
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

#TODO
#调用栈
#没有代码去捕获错误，会一直被抛出，直到被python解释器捕获(反正就是要被捕获，并且有处理的方式）
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')
main()
print('ENd')#这句不会执行，但是main()只有有捕获代码，后面的语句都会执行
#执行结果
'''
Traceback (most recent call last):
  File "err.py", line 11, in <module>
    main()
  File "err.py", line 9, in main
    bar('0')
  File "err.py", line 6, in bar
    return foo(s) * 2
  File "err.py", line 3, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
'''
#TODO
#记录错误，except语句只会执行满足条件后的语句(if XXX: xxx)而打印不了详细的错误信息
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)  #这里会有详细的错误信息，可以通过配置把错误记录到日志文件里？？？怎么配置

main()
print('END')#这句也会执行，并正常退出

#TODO
#抛出错误 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的
#raise 一个实例 except 捕获一个实例 （抛出一个错误，捕获一个错误）
class FooError(ValueError):                             #自定义的一个错误类，从valuerror出继承
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)         #抛出这个错误，并指出错在哪里
    return 10 / n

def bar():
    try:
        foo('0')
    except FooError as e:                               #捕获抛出的这个错误，记录下
        print('ValueError!')
        raise #语句如果不带参数，就会把当前错误原样抛出，让调用者知道怎么处理  #如果没有这句，就值打印ValueError,不会打印一堆的错误来源

bar()

try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!') #错误类型转换