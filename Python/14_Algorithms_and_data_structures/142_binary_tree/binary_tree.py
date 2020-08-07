from node import Node

class Binary_tree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node : Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('The node alreay exists')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
    def search(self, value: int):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return (f'Found {current_node.value}')
            if value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError('We oculd not finf this node')


    def inorder(self):
        self._inorder_recursive(self.head)

    # in debuger mode you can see how it works
    # the return will push you back to the last call you did for that function
    # like this you can read the entire tree
    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)