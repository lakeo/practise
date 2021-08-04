# encoding=utf8

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, nodes):
        self.root = Node(data=nodes[0])
        for i in nodes[1:len(nodes)]:
            self.insert(i)
            pass

    def search(self, node, parent, data):
        if not node:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data < data:
            return self.search(node.right, node, data)
        return self.search(node.left, node, data)

    def insert(self, data):
        flag, node, parent = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data=data)
            if data > parent.data:
                parent.right = new_node
            else:
                parent.left = new_node

    def delete(self, root, data):
        flag, node, parent = self.search(root, root, data)
        if not flag:
            raise Exception('not found')

        if not node.left or not node.right:
            if parent.left == node:
                if node.left:
                    parent.left = node.left
                else:
                    parent.left = node.right
            else:
                if node.left:
                    parent.right = node.left
                else:
                    parent.right = node.right
            del node
        else:
            tmp = node.right
            if tmp.left is None:
                node.data = tmp.data
                node.right = tmp.right
            else:
                pre = tmp
                tmp = tmp.left
                while tmp.left is not None:
                    pre = tmp
                    tmp = tmp.left
                node.data = tmp.data
                self.delete(pre, tmp.data)


