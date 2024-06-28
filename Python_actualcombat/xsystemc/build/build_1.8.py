import time
import json
from file_write import write

user_in = ""
disk = ("A")
version = "1.8"

def cd(disk_name):
    """ 更改当前磁盘 """
    global disk
    if disk_name not in ["A","B","C"]:
        print("disk not found")
    else:
        disk = disk_name


def Loop():
    global user_in,disk
    """ 主命令循环 """
    while True:
        user_in = input(f"command {disk.upper()}:>")
        if user_in == "exit":
            break
        elif user_in == "version":
            print(f"black OS ---------- version {version}")
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
        elif user_in == "clear":
            print("\n" * 100)
        elif user_in == "add":
            user_in = input("")
            a = int(user_in)
            user_in = input("+")
            print("=",a + int(user_in))
        elif user_in == "subtract":
            user_in = input("")
            a = int(user_in)
            user_in = input("-")
            print("=",a - int(user_in))
        elif user_in == "date":
            t = time.localtime()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
            print(current_time)
        elif user_in.startswith("cd "):
            cd(user_in.split(" ")[1])
        elif user_in == "dir":
            with open(r"G:\python_code\Python_actualcombat\xsystemc\file.json","r",encoding="utf-8") as F: # type: ignore
                files = json.load(F)
            print(files[disk])
        elif user_in ==("mf"):
            user_in = input("file name:")
            write(user_in,disk)
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
        elif user_in == "restart":
            print("restarting...")
            time.sleep(1)
            start()
        elif user_in == "lock":
            user_in = input("locking...")
            while True:
                if user_in == "":
                    print("unlocking...")
                    break
        elif user_in == "":
            pass
        else:
            print(f"\"{user_in}\" is not command ")
            time.sleep(1)

def start():
    """ 启动登录流程 """
    global config,user_in
    print("please login")
    user_in = input("user name:")
    if user_in == config['user_name']:
        user_in = input("password:")
        if user_in == config['password']:
            print(f"Hello {config['user_name']}")
            Loop()
        else:
            print("password error")
            time.sleep(1)
    else:
        print("no user")
        time.sleep(1)


config = {"user_name":"admin",
          "password":"123"}

print("-----BLACK OS-----")
print("from xsc at 2023-6-27 19.00")
user_in = input("are you first user? (y/n):")
if user_in == "y":
    print("name => admin")
    print("password => 123")
    start()
else:
    start()