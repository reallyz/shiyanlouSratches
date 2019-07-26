with open('output.txt','a+') as f:
    ls=['how','are','you']
    f.writelines(ls)
    f.seek(0)
    for line in f:
        print(line)

row=0
col=0
with open('/root/桌面/history.txt','r+',encoding='utf-8') as f:
    for line in f:
        print(type(line))
        if line.strip():
            row+=1
            for a in line:
                if a not in "[\\]|,.<>?/:;!\"@#$%^&*()_+-=~`\'\n' '":
                    col+=1
    ls=['zhnong\n','guo\n','hao\n']
    f.writelines(ls)

print(row,col)
#自动轨迹绘制,数据类型的把握,数据和程序的隔离
