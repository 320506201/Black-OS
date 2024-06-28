import time
import json

user_in = ""
disk = ("A")

def cd(disk_name):
    global disk
    disk = disk_name
    if disk != "A" and disk != "B" and disk != "C":
        print("disk not found")


def Loop():
    while True:
        user_in = input(f"command {disk.upper()}:>")
        if user_in == "exit":
            break
        elif user_in == "version":
            print("black OS ---------- version 1.5")
        elif user_in == "help":
            print("""add => add two numbers
cd => come disk to (A,B,C)
clear => clear screen
date => show data
dir => show files
exit => exit black OS
help => show help message
subtract => subtract two numbers
version => show black OS version""")
        elif user_in == "clear":
            print("\n" * 100)
        elif user_in == "add":
            user_in = input("")
            a = int(user_in)
            str(user_in)
            user_in = input("")
            print(a + int(user_in))
        elif user_in == "subtract":
            user_in = input("")
            a = int(user_in)
            str(user_in)
            user_in = input("")
            print(a - int(user_in))
        elif user_in == "date":
            t = time.localtime()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
            print(current_time)
        elif user_in == "cd":
            user_in = input("")
            cd(user_in)
        elif user_in == "dir":
            print(files[disk])
        elif user_in == "":
            pass
        else:
            print("command not found")
            time.sleep(1)

def start():
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


with open(r"G:\python_code\Python_actualcombat\xsystemc\file.json","r",encoding="utf-8") as F: # type: ignore
    files = json.load(F)


print("-----BLACK OS-----")
print("from xsc at 2023-6-27 11.00")
user_in = input("are you first user? (y/n):")
if user_in == "y":
    print("name => admin")
    print("password => 123")
    start()
else:
    start()
