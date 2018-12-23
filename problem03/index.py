import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node, binary_tree_dict=None):
    if node == None:
        return None
    if binary_tree_dict == None:
        binary_tree_dict = {}
    binary_tree_dict['value'] = node.val
    binary_tree_dict['left'] = serialize(node.left)
    binary_tree_dict['right'] = serialize(node.right)

    return json.dumps(binary_tree_dict)

def deserialize(serialize_str):
    if isinstance(serialize_str, str):
        binary_tree_dict = json.loads(serialize_str)
    else:
        binary_tree_dict = serialize_str
    
    if binary_tree_dict == None:
        return None

    val = binary_tree_dict['value']
    left = deserialize(binary_tree_dict['left'])
    right = deserialize(binary_tree_dict['right'])

    return Node(val, left, right)
