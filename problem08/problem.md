# problem

## describe

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

## thought

基本想法是采用二叉树后序遍历，从最后一个结点开始计数，判断一个结点是否为unival subtree 的条件有4:

* 结点为叶
* 结点只有一个子结点且
* 结点有两个子结点且子结点相同
* 如果一个结点不是，那么其所有的父结点都不是unival subtree