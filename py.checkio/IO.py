#read
with open("D:\百家号\复读.jpg",'rb') as r: #还有二进制文件‘rb',还可指定编码encoding=，指定错误处理方式errors=
    print(r.read())
#wirte
with open("D:\百家号\复读.jpg",'w') as w: #mode还有a,追加
    w.write(b'hello world')     #这里的write方法只能写字符串，TypeError: write() argument must be str, not bytes

#在内存中读写，StringIO,BytesIO,对获取到的数据进行操作，但是并不想把数据写到本地硬盘
from io import StringIO
st=StringIO()
st.write('hello')
st.write(' world!')
print(st.getvalue())#读取所有的输入
from io import BytesIO
bt=BytesIO()
bt.write('中文'.encode('utf-8')) #这里的write方法只能写二进制数
print(bt.getvalue())#读取所有的输入
###精彩的地方开始了###
from io import StringIO
f = StringIO()
f.write('Hello World')
s = f.readline()
print(s) #这里进行读，读取不到任何内容
'''
#原因：the stream position
d=StringIO('hello world')
stream position 为0（可以通d.tell()获得stream position)
d.readline() stream position 移动到11
再次执行d.readline()时，从stream position 11开始，而11后为空 
可以通过d.seek()调整stream position
# tell 方法获取当前文件读取指针的位置
# seek 方法，用于移动文件读写指针到指定位置,有两个参数，
第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；
第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
# 用seek方法时，需注意，如果你打开的文件没有用'b'的方式打开，则offset无法使用负值
'''
f = StringIO("1\n2\n3")
f.write("4\n 5\n 6")
f.seek(0)
while True:
    s = f.readline()
    if s == "":
        break
    print(s.strip())
#output为4，5，6，原因在于，write()方法是从指针为0的地方开始追加，会覆盖之前(SringIO())中输入的内容
