import time

def Loop():
    while True:
        user_in = input("command >")
        if user_in == "exit":
            break
        elif user_in == "load":
            user_load_time = int(input("load time:"))
            print("load now")
            time.sleep(user_load_time)
        elif user_in == "version":
            print("xsystemc version ---------- 1.2")
        elif user_in == "help":
            print("""exit => exit xsystemc
load => load xsystemc to some seconds
version => show xsystemc version""")
        else:
            print("command not found")
            time.sleep(1)



config = {"user_name":"admin",
                "password":"123"}


print("                    Welcome to xsystemc")
print("from xsc at 2023-6-26")
user_in = input("are you first user? (y/n):")
if user_in == "y":
    print("name => admin")
    print("password => 123")
else:
    user_in = input("user name:")
    if user_in == config['user_name']:
        user_in = input("password:")
        if user_in == config['password']:
            print("Welcome")
            Loop()
        else:
            print("password error")
            time.sleep(1)
    else:
        print("no user")
        time.sleep(1)
