import  re
ls=re.findall(r'[0-9]\d{5}','BIT 100081')
if ls:
    print(ls)

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
