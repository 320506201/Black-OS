text = {"morning":"早上",
        "afternoon":"下午",
        "evening":"晚上，傍晚",
        "night":"夜晚",
        "Miss":"小姐",
        "mum":"妈妈",
        "dad":"爸爸",
        "this":"这个",
        "is":"是",
        "Mr":"先生",
        "a":"一个",
        "teddy":"泰迪熊",
        "box":"盒子",
        "yes":"是的，对的",
        "bag":"包",
        "no":"不，不是，没有",
        "puppy":"小狗",}
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