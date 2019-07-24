

#局部变量和全局变量
#局部变量为组合数据类型（就是里面什么类型都可以放），
#且未创建，等同于全局变量
ls=['F','f']#全局变量
def funls(a):
    ls.append(a)  #没有改指针
    return
funls('c') #全局变量被修改

def funs(a):
    ls=[]    #已经创建，有了新的指针?
    ls.append(a)
    return

n,s=1,5
def p(o):
    global s
    s=s+o
    print(o+s)
    return
p(10)

#digit tube
import time
import turtle
def drawLine(draw):   #绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(digit): #根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):  #获得要输出的数字
    w={'+':'日','-':'年','=':'月'}
    for i in date:
        if i in w:
            turtle.write(w[i],font=('Arial',18))
            turtle.fd(60)
            turtle.pencolor('blue')
        else:
            drawDigit(eval(i))  #通过eval()函数将数字变为整数
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
