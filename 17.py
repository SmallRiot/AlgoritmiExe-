#Построение дерева формулы, заданной в префиксной форме (+ 1 2)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while current:
            if current.data == data:
                return
            elif current.data > data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def print_tree(self, current_node, level=0):
        if not current_node:
            return
        self.print_tree(current_node.right, level + 1)
        print(' ' * 10 * level + '->', current_node.data)
        self.print_tree(current_node.left, level + 1)

def build_tree(formula):
    tree = Tree()
    for i in formula:
        tree.add(i)
    return tree

def main():
    formula = ['+', 1, 2]
    tree = build_tree(formula)
    tree.print_tree(tree.root)


