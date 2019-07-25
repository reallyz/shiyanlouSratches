with open('output.txt','a+') as f:
    ls=['how','are','you']
    f.writelines(ls)
    f.seek(0)
    for line in f:
        print(line)


#自动轨迹绘制,数据类型的把握
