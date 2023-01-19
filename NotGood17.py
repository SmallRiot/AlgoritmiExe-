from treelib import Tree

def build_tree(expression):
    # create a new tree
    tree = Tree()
    # add the root node
    tree.create_node(expression[0], "root")

    def build_tree_rec(parent, i):
        if i>=len(expression):
            return
        if expression[i] in "+-*/":
            tree.create_node(expression[i], i, parent)
            build_tree_rec(i, i+1)
            build_tree_rec(i, i+2)
        else:
            tree.create_node(expression[i], i, parent)
    build_tree_rec("root", 1)
    tree.show()

expression = ["*","+","3","4","5"]
build_tree(expression)
