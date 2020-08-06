
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9790256#overview
from node import Node
from binary_tree import Binary_tree

tree = Binary_tree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

print(tree.head)
print(tree.head.left)
print(tree.head.right)