text = {"单选":"1~2",
        "排序":"4~8",
        "填空":"1",
        "阅读":"1~5"}

query = input("题目分数查询：")
if query in text:
    print("题目：" + query + "，分数：" + text[query])
else:
    print("Error: " + "don\'t have")
    print("当前有" + str(len(text)) + "种题目")