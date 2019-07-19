#make a little difference very day
print(pow(1.01,365))
print(pow(0.99,365))
print('very powerful')
dayfactor=float(input())
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print(dayup)
print(daydown)
#5天进步2天退步
du=1.0
df=0.01
for i in range(365):
    if i%7 in [6,0]:
        du=du*(1-df)
    else:
        du=du*(1+df)
print(du)
#工作日需要多努力才能和每天都努力比阶
def dayUp(df):
    ddup=1
    for i in range(365):
        if i%7 in[6,0]:
            ddup=ddup*(1-0.01)
        else:
            ddup=ddup*(1+df)
    return ddup
ddf=0.01
while dayUp(ddf)<37.78:
    ddf=ddf+0.001
print('you must work harder than:{:.3f}'.format(ddf))