
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9790256#overview
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9790264#overview
# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9790266#overview

from node import Node
from binary_tree import Binary_tree

tree = Binary_tree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

#print(tree.head)
#print(tree.head.left)
#print(tree.head.right)

# this will read the three with one of the 3 methods for reading
tree.inorder()

print(tree.search(11))