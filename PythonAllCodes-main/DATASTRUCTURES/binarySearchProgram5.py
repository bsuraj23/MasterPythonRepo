def binary_search(arr, target):
    # Binary search works on sorted arrays
    # It repeatedly divides the search interval in half
    left, right = 0, len(arr) - 1  # Initialize pointers to start and end of array
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Target found, return its index
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    # Target not found, return -1
    return -1

# Demo usage
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    target = 7
    result = binary_search(arr, target)
    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in array")
class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
