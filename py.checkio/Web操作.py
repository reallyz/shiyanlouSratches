
#urllib

from urllib import  request,parse

with request.urlopen('https://zhidao.baidu.com/question/347704438.html') as f: #使用默认格式直接打开url
    data=f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k, v))

    print('Data:', data.decode('unicode-escape'))

#模拟浏览器发送GET请求，使用Request对象
req=request.Request('http://www.douban.com/')     #构建一个request对象
req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')#修饰这个对象
with request.urlopen(req) as f:                 #使用这个对象
    print('Statu:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print("Data:",f.read().decode('utf-8'))

#模拟登录，Post
print('Login to weibo.com')
account=input('Account:')
passwd=input('Password:')
login_data=parse.urlencode([            #使用POst方法需要构建数据结构,把要post的数据放进去
    ('username', account),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

