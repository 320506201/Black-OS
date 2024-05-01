import random
import time

keyboard = input("start继续,quit退出")
if keyboard == "quit":
    print("退出游戏")
    exit()
else:
    print("游戏开始")
print("勇者你好")
name = input("请输入你的名字：")
print("你好，" + name )

xp = 0
hp = 100    
level = 1
menny = 100
midicine = 0
boss_hp = 1000
i = 1
print("你来到了一片荒芜之地，你发现了一条小路，你决定前进。")
print("你走了很久，终于来到了一座山顶，你发现了一条通往山脚的小路。")
print("一位少女被拖走，你决定去救她。")

def gameloop():
    global xp, hp, level, menny, midicine, boss_hp,i
    while True:
        if hp <= 0:
            print("你死了！")
            return ()
        else:
            if xp >= 100:
                level += 1
                xp -= 100
                hp += 10
                menny += 10
                print("恭喜升级！")
            print("你目前的经验值：" + str(xp) + "，生命值：" + str(hp) + "，等级：" + str(level) + "，金钱：" + str(menny) + ",血包：" + str(midicine))
            print("1.攻击")
            print("2.购买物品")
            print("3.boss战")
            print("4.退出游戏")
            print("5.回血")
            choice = input("请输入你的选择：")
            enemy_hp = 100
            if choice == "1":
                while enemy_hp > 0:
                    print("你攻击了敌人！")
                    enemy_hp -= random.randrange(10,50,10)
                    if enemy_hp <= 0:
                        print("你击败了敌人！")
                        hp -= random.randrange(10,50,10)
                        xp += random.randrange(10,50,10)
                        menny += random.randrange(10,50,10)
                        gameloop()
                    else:
                        print("敌人剩余生命：" + str(enemy_hp))
                        print("你还有" + str(hp) + "生命值")
                    time.sleep(0.5)
            elif choice == "2":
                if menny >= 10:
                    print("已购买血包")
                    midicine += 2
                    menny -= 10
                else:
                    print("金钱不足！")
            elif choice == "3":
                while boss_hp or hp >= 0:
                    print("你进入了boss战")
                    boss_hp -= random.randrange(10,60,10)
                    hp -= random.randrange(10,70,10)
                    if boss_hp <= 0:
                        print("你击败了boss")
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        menny += 1000
                        xp += 1500
                        boss_hp = 1000 * i
                        i += 1
                        return ()
                    else:
                        print("boss剩余生命:" + str(boss_hp))
                        print("你还有" + str(hp) + "生命值")
                    if hp <= 0:
                        print("你死了！")
                        return ()
                    time.sleep(0.1)
            elif choice == "4":
                print("再见" + name )
                return ()
            elif choice == "5":
                if midicine > 0:
                    hp += 20
                    midicine -= 1
                else:
                    print("你没有血包！")
                    
gameloop()