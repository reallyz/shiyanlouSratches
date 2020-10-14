import requests
#获取信息
#get方法,通用代码框架，更稳定的可靠,异常处理很重要

def gethtml(url,**para):#**para是一个dict
    #headr={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    try:
        r=requests.get(url,para)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r
    except:
        print('获取失败')
        return None


if __name__=='__main__':
    #百度搜索
    urlbd='https://www.baidu.com/s'
    keyword = 'Python'
    para = {'wd': keyword}
    r=gethtml(urlbd,para=para)
    print(r.request.url)
    print(len(r.text))
    #图片保存
    import os
    import time
    urljpg='https://wx2.sinaimg.cn/mw690/67338b16gy1g5bamwnw36j21hc0u0b2d.jpg'
    j=gethtml(urljpg)
    print(j.request.url)
    dir='/root/图片/'
    path=dir+str(int(time.time()))+'.jpg'
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)
        if not os.path.exists(path):
            with open(path,'wb') as f:
                f.write(j.content)
        else:
            print('文件已经存在')
    except:
        print('unknown error')
    #ip地址判断,需要API接口
    ip='118.114.2.1'
    urlip='http://www.ip138.com/ips138.asp?ip='+ip
    p=gethtml(urlip)
    print(p.text[:1000])
