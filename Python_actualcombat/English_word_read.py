text = {"Miss":"小姐",
        "class":"同学们",
        "I":"我",
        "I\'m":"I am",
        "are":"是",
        "you":"你",
        "yes":"是；对",
        "am":"是",
        "no":"不；不是；没有",
        "not":"不；没有",
        "my":"我的",
        "friend":"朋友",}
x = 0

def e ():
    query = input("单词含义查询：")
    if query in text:
        print("单词：" + query + "，含义：" + text[query])
        x = input()
        if x == "离开":
            return 0
        else :
            e()
    else:
        print("Error: " + "don\'t have")
        print("当前有" + str(len(text)) + "个单词")
        x = int(input())
        if x == 1 :
            return 0
        else :
            e()

print("该文件来自译林版英语书。")
e()