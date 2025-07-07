class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.val == key:
            return True
        elif key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

bst = BinarySearchTree()
while(1):
    print("1.For Insert Node")
    print("2.For Search Node")
    print("0.For Exit")
    print("----------------")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        x=int(input("Enter elements:"))
        bst.insert(x)
    elif ch==2:
        key=int(input("Enter an element you want to search:"))
        bst.search(key)
        if bst.search(key):
          print(f"Element {key} found in the BST.")
        else:
          print(f"Element {key} not found in the BST.")
    elif ch==0:
        print("Exit From The Program")
        break
    else:
        print("Invalid choice.Enter the correct choice.")
