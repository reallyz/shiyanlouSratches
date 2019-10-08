
# more details about python

'''
python source:
# Include: python's all head file
# Lib:python's standard library
# Modules: code in C more effective
# Parser:Scanner and Parser
# Python:python compiler
'''

'''
# 1 python： .py -->(编译器)-->.pyc-->解释器(虚拟机)-->结果
compile and disassemble
'''
source_code=\
'''
#this is for compile directly
def test1(a,b):
    return a+b
def test2(c):
    x=7
    print(c**2+x)
'''
co=compile(source_code,'/root/test_compile.py','exec')
exec(co)
test2(3)
import  dis

dis.dis(co)
