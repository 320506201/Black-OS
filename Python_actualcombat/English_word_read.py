import json
with open ("/Users/apple/Desktop/python_code/Python_actualcombat/English_word.json","r") as fp:
    text = json.load(fp)
    print (text)
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
        print("当前有" + str(len(text)) + "个单词")
        x = int(input())
        if x == 1 :
            return 0
        else :
            e()

print("该文件来自译林版英语书。")
e()