import turtle
def drawgap():#绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawline(draw):#绘制单段数码管，由draw是否为真判断是移动还是画线
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)
def drawdigit(digit):#根据数字绘制七段数码管
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()#为绘制后续数字确定位置
    turtle.fd(20)#为绘制后续数字确定位置
def drawdate(date):#获得要输入的数字
    for i in date:
        drawdigit(eval(i))#将字符串拆成一个一个并绘制
def main():
    turtle.tracer(False)
    turtle.setup(1000,350,200,200)
    turtle.penup()
    turtle.pencolor('purple')
    turtle.speed(0)
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate('20181307')
    turtle.hideturtle()
    turtle.done()
main()
