"""
二叉树：
    1. 每个节点最多有两个孩子节点
    2. 每个孩子节点被命名为左孩子或右孩子
    3. 对于每个节点的孩子节点，在顺序上，左孩子优于右孩子
"""
from abstractTree import Tree
class BinaryTree(Tree):
    """Abstract base classs representing a binary tree structure."""
    def left(self,p):
        """Return a Position representing p`s left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')
