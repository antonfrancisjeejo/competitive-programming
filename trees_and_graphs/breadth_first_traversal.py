class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def level_order_traversal(self, root):
        h = self.height(root)
        for i in range(1, h + 1):
            self.print_level(root, i)

    def print_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")
        elif level > 1:
            self.print_level(root.left, level - 1)
            self.print_level(root.right, level - 1)


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)
root.insert(20)
root.level_order_traversal(root)
