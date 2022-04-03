# Binary Tree in Python
# Node has three components - left (another Node), right (another Node), and value

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder - print yourself, then do left and/or right
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder - do left if it exists, then print yourself, then right if it exists
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder - do left and/or right, and then print yourself
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

#     1
#    / \
#   2   3
#  /
# 4

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
# This is 1... 2... 4... 3
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
# This is 4... 2... 1... 3
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
# This is 4... 2... 3... 1
root.traversePostOrder()