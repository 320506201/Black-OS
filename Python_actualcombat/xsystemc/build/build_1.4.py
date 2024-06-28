import time

user_in = ""

def Loop():
    while True:
        user_in = input("command >")
        if user_in == "exit":
            break
        elif user_in == "version":
            print("black OS ---------- version 1.4")
        elif user_in == "help":
            print("""add => add two numbers
clear => clear screen
date => show data
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
            print("Hello")
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
print("from xsc at 2023-6-27 10.00")
user_in = input("are you first user? (y/n):")
if user_in == "y":
    print("name => admin")
    print("password => 123")
    start()
else:
    start()
