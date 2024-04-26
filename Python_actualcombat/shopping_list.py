shopping_list = []
print("1 = 退回， 2 = 开始")
def all ():
    a = int(input("1或2\n"))
    if a >= 2:
        shopping_list.append(input("物品\n"))
        print(shopping_list)
    else:
        print("bye")
        f = open('test.txt','w',)
        f.write(str(shopping_list) +'\n')
        f.close()
        return()
    all()


all()