from urllib.request import urlopen


class UrlTemplate(object):
    def __init__(self,template):
        self.template=template
    def open(self,**kwargs):
        return urlopen(self.template.format_map(kwargs))
fi='http://finance.sina.com.cn/realstock/company/{code}/nc.shtml'
code={'code':'sh000003'}
sina=UrlTemplate(fi)
for line in sina.open(code='sh000003'):
    try:
        print(line.decode('utf-8'))
    except:
        print('exception')

#闭包的方式实现，实际上只有一个方法的类是为了保存环境信息
#而闭包就是可以保存环境信息
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

sinain=urltemplate(fi)
print(type(sinain))
for line in sinain(code='sh000003'):
    try:
        print(line.decode('utf-8'))
    except:
        print('exception')