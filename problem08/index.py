class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_unival_tree(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    total_count = count_unival_tree(root.left) + count_unival_tree(root.right) 
    if root.left == None or root.right == None:
        if (root.left and root.left.data == root.data) or (root.right and root.right.data == root.data):
            total_count += 1
    elif root.data == root.right.data == root.left.data:
        total_count += 1
    return total_count