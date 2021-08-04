# encoding=utf8

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.depth = 0
        self.parent = None

class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        if not self.root:
            raise Exception('empty')
        return self._find(key, self.root)

    def _find(self, key, node):
        if not node:
            raise Exception('not found')
        if node.data == key:
            return node
        if key < node.data:
            return self._find(key, node.left)
        return self._find(key, node.right)

    def height(self, node):
        if not node:
            return -1
        return node.height

    def singleRight(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        left.height = max(self.height(left.right), self.height(left.left)) + 1
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return left

    def singleLeft(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        right.height = max(self.height(right.right), self.height(right.left)) + 1
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return right

    def LR(self, node):
        self.singleLeft(node.left)
        return self.singleRight(node)

    def RL(self, node):
        self.singleRight(node.left)
        return self.singleLeft(node)

