# encoding=utf8

class Node:
    def __init__(self):
        self.is_left = False
        self.nodes = {}
        self.count = 0

class Tree:
    def __init__(self):
        self.root = Node()

    def insert_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = Node()
                curr = curr.nodes[c]
        curr.is_left = True
        curr.count += 1

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                return None
            curr = curr.nodes[c]
        if curr.is_left:
            return curr
        return None

