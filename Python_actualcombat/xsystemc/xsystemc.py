#引入模块
import time
import json
import configparser
#定义变量
user_in = ""
disk = ("A")
version = "2.0"
config = configparser.ConfigParser()
config.read(r"G:\python_code\Python_actualcombat\xsystemc\config.ini")
user_name = config['DEFAULT']["user_name"]
password = config['DEFAULT']["password"]
all_disk = config['DEFAULT']["all_disk"]
are_first = config['DEFAULT'].getboolean('are_first')
#定义函数
def cd(disk_name):
    """ 更改当前磁盘 """
    global disk
    if disk_name not in all_disk:
        print("disk not found")
    else:
        disk = disk_name

def Loop():
    global user_in,disk
    """ 主命令循环 """
    while True:
        #开始
        user_in = input(f"command {disk.upper()}:>")
        #A
        if user_in == "add":
            user_in = input("")
            a = int(user_in)
            user_in = input("+")
            print("=",a + int(user_in))
        #b
        #c
        elif user_in.startswith("cd "):
            cd(user_in.split(" ")[1])
        elif user_in == "clear":
            print("\n" * 100)
        #d
        elif user_in == "date":
            t = time.localtime()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
            print(current_time)
        elif user_in == "df":
            user_in = input("file name:")
            with open(r"G:\python_code\Python_actualcombat\xsystemc\file.json","r",encoding="utf-8") as F: # type: ignore
                files = json.load(F)
            if user_in in files[disk]:
                files[disk].remove(user_in)
            else:
                print("file not found")
            with open(r"G:\python_code\Python_actualcombat\xsystemc\file.json","w",encoding="utf-8") as F: # type: ignore
                json.dump(files,F)
        elif user_in == "dir":
            with open(r"G:\python_code\Python_actualcombat\xsystemc\file.json","r",encoding="utf-8") as F: # type: ignore
                files = json.load(F)
            print(files[disk])
        #e
        elif user_in == "exit":
            break
        #f
        #g
        #h
        elif user_in == "help":
            print("""    add => add two numbers
    cd => come disk to (A,B,C)
    df => delete a file
    mf => make a file
    clear => clear screen
    date => show data
    dir => show files
    exit => exit black OS
    help => show help message
    lock => lock black OS
    restart => restart black OS
    subtract => subtract two numbers
    version => show black OS version""")
        #i
        #j
        #k
        #l
        elif user_in == "lock":
            user_in = input("locking...")
            while True:
                if user_in == "":
                    print("unlocking...")
                    break
        #m
        elif user_in ==("mf"):
            user_in = input("file name:")
            write(user_in,disk)
        #n
        #o
        #p
        #q
        #r
        elif user_in == "restart":
            print("restarting...")
            time.sleep(1)
            start()
        #s
        elif user_in == "subtract":
            user_in = input("")
            a = int(user_in)
            user_in = input("-")
            print("=",a - int(user_in))
        #t
        #u
        #v
        elif user_in == "version":
            print(f"black OS ---------- version {version}")
        #w
        #x
        #y
        #other
        elif user_in == "":
            pass
        else:
            print(f"\"{user_in}\" is not command ")
            time.sleep(1)

def start():
    """ 启动登录流程 """
    global user_name,password,user_in
    print("please login")
    user_in = input("user name:")
    if user_in == user_name:
        user_in = input("password:")
        if user_in ==password:
            print(f"Hello",user_name)
            Loop()
        else:
            print("password error")
            time.sleep(1)
    else:
        print("no user")
        time.sleep(1)            

def write(date,adder):
    with open(r"G:\python_code\Python_actualcombat\xsystemc\file.json", 'r') as f:
        wait = json.load(f)
    wait[adder].append(date)
    with open(r"G:\python_code\Python_actualcombat\xsystemc\file.json", 'w') as f:
        json.dump(wait, f)
#启动程序
print("          -----BLACK OS-----")
print("from xsc at 2023-6-28 10.00")
if are_first == True:
    print("admin password is 123")
    config["DEFAULT"].update({"are_first": "False"})
    with open(r"G:\python_code\Python_actualcombat\xsystemc\config.ini","w") as configfile:
        config.write(configfile)
    start()
else:
    start()