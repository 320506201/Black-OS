import turtle

# 创建画布
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# 创建一个小乌龟
tess = turtle.Turtle()
tess.speed(0)  # 设置速度为最快

# 使用tracer关闭动画
wn.tracer(0)

# 移动小乌龟的函数
def move_turtle():
    tess.forward(5)
    wn.update()  # 更新画布

    # 继续移动小乌龟
    wn.ontimer(move_turtle, 10)

# 调用移动函数
move_turtle()

# 运行
turtle.done()
