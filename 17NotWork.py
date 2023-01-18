class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.value)

class PrefixTree:
    def __init__(self):
        self.root = None

    def constructTree(self, prefix):
        stack = []
        # Iterating the prefix expression from right to left
        for char in prefix[::-1]:
            # if the character is an operator
            if char in ["+", "-", "*", "/"]:
                # pop two elements from the stack
                right = stack.pop()
                left = stack.pop()
                # create a new operator node with the popped elements as children
                node = Node(char)
                node.right = right
                node.left = left
                # push the new operator node back onto the stack
                stack.append(node)
            # if the character is an operand
            else:
                # create a new operand node and push it onto the stack
                node = Node(char)
                stack.append(node)
        # the final node in the stack is the root of the constructed tree
        self.root = stack.pop()
        
    def display(self, root, level=0):
        if root is not None:
            self.display(root.left, level + 1)
            print(' ' * 4 * level + '->', root.value)
            self.display(root.right, level + 1)

# create an instance of the PrefixTree class
pt = PrefixTree()
# construct the tree
pt.constructTree("*+3+45")
# display the tree
print("prefix expression tree:")
pt.display(pt.root)
