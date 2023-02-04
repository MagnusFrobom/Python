class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_inorder(node):
    if node is not None:
        print_inorder(node.left)
        print(node.value)
        print_inorder(node.right)


root = Node(1, Node(2, Node(4), Node(5)), Node(3))
print_inorder(root)  # 4 2 5 1 3
