class node:
    def init(self, c):
        self.data = c
        self.left = self.right = None


# Function to recursively build the expression tree
def add(a):
    # If its the end of the expression
    if (a == ''):
        return ''

    # If the character is an operand
    if a[0] >= 'a' and a[0] <= 'z':
        return node(a[0]), a[1:]
    else:
        # Create a node with a[0] as the data and
        # both the children set to null
        p = node(a[0])
        # Build the left sub-tree
        p.left, q = add(a[1:])
        # Build the right sub-tree
        p.right, q = add(q)
        return p, q




#function to print tree in console
def print_tree(node, level=0):
    if node:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.data)
        print_tree(node.left, level + 1)

# Driver code
if __name__ == '__main__':
    a = "*+ab-cd"
    s, a = add(a)
    print_tree(s)