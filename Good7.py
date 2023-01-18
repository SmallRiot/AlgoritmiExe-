class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Добавляет новое значение в дерево 
        """
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value > current_node.value:
                    if not current_node.right:
                        current_node.right = new_node
                        break
                    current_node = current_node.right
                else:
                    if not current_node.left:
                        current_node.left = new_node
                        break
                    current_node = current_node.left

    def print_tree(self, current_node, level=0):
        """
        Рекурсивно обходит дерево и печатает его с учетом уровня вложенности
        """
        if not current_node:
            return
        self.print_tree(current_node.right, level + 1)
        print(' ' * 10 * level + '->', current_node.value)
        self.print_tree(current_node.left, level + 1)

# Пример использования
arr = [3, 5, 2, 7, 1, 4, 6, 8]
tree = BinaryTree()
for value in arr:
    tree.insert(value)
tree.print_tree(tree.root)
