class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# Demo usage
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    print("Inorder traversal:")
    inorder(root)
    print()

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# Build Tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

inorder(root)  # 5 10 15
