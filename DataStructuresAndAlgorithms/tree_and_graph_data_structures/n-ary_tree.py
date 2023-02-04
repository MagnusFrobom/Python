class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


def print_preorder(node):
    if node is not None:
        print(node.value)
        for child in node.children:
            print_preorder(child)


root = Node(1, [Node(2, [Node(4), Node(5)]), Node(3)])
print_preorder(root)  # 1 2 4 5 3