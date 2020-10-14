import  re
ls=re.findall(r'[0-9]\d{5}','BIT 100081')#信息提取的时候很好用
if ls:
    print(ls)
#findall,finditer都是多次匹配，一个输出的是列表，一个输出迭代对象
for m in re.finditer(r'[1-9]\d{5}','e100081 r100082'):
    if m:
        print(m.group(0))

s=re.sub(r'[1-9]\d{5}','zz','e100081 r100082')
print(s)

#match对象
match=re.search(r'[0-9]\d{5}','BIT 100081')
if match:
    print(match)

#最小匹配：*?,+?,??.{m,n}?,以?限制
