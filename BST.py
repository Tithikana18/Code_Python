class Tree:
    def __init__(self,data):
        self.data=data
        self.l=None
        self.r=None
class Bst_Tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=Tree(data)
        else:
            self.insert1(self.root,data)
    def insert1(self,node,data):
        if data<node.data:
            if node.l is None:
                node.l=Tree(data)
            else:
                self.insert1(node.l,data)
        else:
            if node.r is None:
                node.r=Tree(data)
            else:
                self.insert1(node.r,data)
    def inorder(self):
        result=[]
        self._inorder_helper(self.root,result)
        return result
    def _inorder_helper(self,node,result):
        if node:
            self._inorder_helper(node.l,result)
            result.append(node.data)
            self._inorder_helper(node.r,result)
    def preorder(self):
        result=[]
        self._preorder_helper(self.root,result)
        return result
    def _preorder_helper(self,node,result):
        if node:
            result.append(node.data)
            self._preorder_helper(node.l,result)
            self._preorder_helper(node.r,result)
    def postorder(self):
        result=[]
        self._postorder_helper(self.root,result)
        return result
    def _postorder_helper(self,node,result):
        if node:
            self._postorder_helper(node.l,result)
            self._postorder_helper(node.r,result)
            result.append(node.data)
bst=Bst_Tree()
while(1):
    print("1.For Create Tree")
    print("2.For Inorder")
    print("3.For Preorder")
    print("4.Foe Postorder")
    print("0.For Exit")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        x=int(input("Enter an element:"))
        bst.insert(x)
    elif ch==2:
        print("Inorder Traversal:",bst.inorder())
    elif ch==3:
        print("Preorder Traversal:",bst.preorder())
    elif ch==4:
        print("Postorder Traversal:",bst.postorder())
    elif ch==0:
        print("Exit From The Program:")
        break
    else:
        print("Invalid choice.Please enter correct choice")
        
