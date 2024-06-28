import json
with open ("Python_actualcombat\English_word.json","r",encoding='utf-8') as fp: # type: ignore
    text = json.load(fp)
x = 0

def e ():
    query = input("单词含义查询：")
    print("1退出2继续")
    if query in text:
        print("单词：" + query + "，含义：" + text[query])
        x = int(input())
        if x == 1:
            return 0
        else :
            e()
    else:
        print("Error: " + "don\'t have")
        print("当前有" + str(len(text)-1) + "个单词")
        x = int(input())
        if x == 1 :
            print("good bye")
            return 0
        else :
            e()

print("该文件来自译林版英语书。")
e()