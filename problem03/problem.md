# problem03

## describe

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:*

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

## thought

遍历树然后组成一个dict，利用json库将其json序列化成字符串，反序列化就是利用json将其反序列化然后生成dict，遍历dict生成node。关于node类，题目中并没有要求自建的node类，只是给出一个node的根结点，如果自建node类的话，那么node类除了例中三个属性之外应该还有一个插入的方法