import random

x = random.randrange(0,100,1)
y = int(input("0~100中的一个数: "))
z = 0

def a():
    global y,z
    while x != y & z != 10:
        if y > x:
            print("大了")
        if y < x:
            print("小了")
        if y == x:
            return
        z = z + 1
        print(10 - z)
        y = int(input("再来：  "))
    
a()

if z == 10:
    print("Game Over")
else:
    print("WIN")
