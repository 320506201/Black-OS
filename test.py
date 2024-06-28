class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

# 创建树节点
root = TreeNode("Root")

C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
python_code = TreeNode("python_code")
铃声 = TreeNode("铃声")
# 添加子节点

root.add_child(C)

root.add_child(D)
D.add_child(python_code)
D.add_child(铃声)

root.add_child(E)

# 打印树结构
print(root)
