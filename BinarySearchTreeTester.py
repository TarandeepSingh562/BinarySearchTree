"""
This test file tests the binary search tree to see if its working correctly -- The test inserts and
finds the height of tree, size of tree, and maximum value of the tree
"""

from BinarySearchTree import *



root = Node(3)
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 5)
root = insert(root, 4)
root = insert(root, 6)
root = insert(root, 7)

maxDepth = height(root)
height = maxDepth
print("The height of the tree is: " + str(height))
maxSize = size(root)
size = maxSize
print("The size of the tree is: " + str(size))
maxValue = maximum(root)
maximum = maxValue
print("The maximum value of the tree is: " + str(maximum))


"""
The height of the tree is: 3
The size of the tree is: 7
The maximum value of the tree is: 7
"""
