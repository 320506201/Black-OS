class student:  # 定义一个学生类
    def __init__(self, name, age, grade, class_name, book_in):  # 初始化方法，设置学生的各项属性
        self.name = name  # 学生的姓名
        self.age = age  # 学生的年龄
        self.grade = grade  # 学生的年级
        self.class_name = class_name  # 学生所在的班级名称
        self.book_in = book_in  # 学生当前阅读的书籍

class administrator():  # 定义一个管理员类
    def __init__(self, name):  # 初始化方法，设置管理员的属性
        self.name = name  # 管理员的名字


def prompt_exit():
    # 提示用户确认退出系统
    if input("按键 'y' 确认退出系统，按其他键继续运行: \n").lower() == 'y':
        exit()

students = {
    43000001 : administrator("admin"),
    43190301 :student("何家豪",11,5,3,0),
    43190302 :student("郭威辰",11,5,3,0),
    43190303 :student("徐晨轩",11,5,3,0),
    43190304 :student("王思懿",11,5,3,0),
    43190305 :student("方学槿",11,5,3,0),
    43190306 :student("于成",11,5,3,0),
    43190307 :student("王启涵",11,5,3,0),
    43190308 :student("龚晟轩",11,5,3,0),
    43190309 :student("应传宏",11,5,3,0),
    43190310 :student("李梓堃",11,5,3,0),
    43190311 :student("林柏桓",11,5,3,0),
    43190312 :student("许思宸",11,5,3,0)
}

# 书籍信息
books ={"1":"语文一上", 
        "2":"数学一上", 
        "3":"体育一上"}

print("                           借阅书籍管理系统")

# 设置管理员的基本信息
print( "管理员信息：", students[43000001].name)
while True:
    user = int(input("请输入学号:\n"))
    if user in students:
        if user == 43000001:
            print("欢迎管理员", students[user].name, "!")
            system_in = int(input("""输入操作:
                            1.退出系统\n"""))
            if system_in == 1:
                prompt_exit()
            else:
                print("输入错误！")
        else:
            print("欢迎", students[user].name, "同学！")
            system_in = int(input("""输入操作:
                            1. 借阅书籍
                            2. 归还书籍
                            3.退出系统\n"""))
            if system_in == 1:
                book_id = input("请输入书籍ID:\n")
                if book_id in books:
                    students[user].book_in += 1
                    print("欢迎您，", students[user].name, "同学！您已成功借阅", books[book_id], "一本。")
                else:
                    print("书籍不存在！")
            elif system_in == 2:
                if students[user].book_in > 0:
                    students[user].book_in -= 1
                    print("欢迎您，", students[user].name, "同学！您已成功归还一本书。")
                else:
                    print("您还没有借阅书籍！")
            elif system_in == 3:
                if user == 43000001:
                    prompt_exit()
                else:
                    print("您不是管理员，无权退出系统！")
            else:
                print("输入错误！")
    else:
        print("您输入的学号不存在！")