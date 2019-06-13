import unittest
from mydict import Dict
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setup!')
    def tearDown(self):
        print('tear down!')
    def test_init(self):                        #每一类测试的方法
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):         #with函数：先把函数开着，执行完自动释放
            value = d.empty

if __name__=='__main__':
    unittest.main()            #在命令行执行：python -m unittest unitest 命令行可以一次性运行很多单元测试

'''
class TestDict(unittest.TestCase):

    def setUp(self):                #setUp(),tearDown(),每一个测试方法都需要用到一个外部接口时。这两个
                                        函数会在每调用一个测试方法前后分别执行
        print('setUp...')

    def tearDown(self):    
        print('tearDown...')
'''