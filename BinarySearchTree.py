"""
This python file contains a binary search tree with functions such as height, size, maximum(for element in tree), min, and delete.
"""

class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def min(node):
    curr = node
    while curr.left is not None:
        curr = curr.left
    return curr


def delete(root, currNode):
    if root is None:
        return currNode
    elif root.data < currNode.root:
        currNode.left = delete(root.left, currNode)
    elif root.data > currNode.root:
        currNode.right = delete(root.right,currNode)
    else:
        if root.left is None:
            t = root.right
            root = None
            return t

        elif root.right is None:
            t = root.left
            root = None
            return t
    t = min(root.right)
    root.data = t.data
    root.right = delete(root.right, t)

    return root


def search(root, data):
    if root:
        if root.data > data:
            return search(root.left, data)
        elif root.data < data:
            return search(root.right, data)
        else:
            return True
    return False


def height(node):
    if node is None:
        return -1
    else :
        lDepth = height(node.left)
        rDepth = height(node.right)
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1


def size(root):
    if root is not None:
        return 1 + size(root.right) + size(root.left)
    elif root is None:
        return 0
      

def maximum(node):
    curr = node
    while curr.right is not None:
        curr = curr.right
    return curr.data
  

def pre_order(root):
    if not root:
        return None
    else:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)


def in_order(root):
    if not root:
        return None
    else:
        in_order(root.left)
        print(root.data)
        in_order(root.right)


def post_order(root):
    if not root:
        return None
    else:
        post_order(root.left)
        post_order(root.right)
        print(root.data)
