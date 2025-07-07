class Node:
    def __init__(self,coff,exp):
        self.coff=coff
        self.exp=exp
        self.next=None
class Polynomial:
    def __init__(self):
        self.head=None
    def insert(self,coff,exp):
        p=self.head
        q=Node(coff,exp)
        if p==None:
            self.head=q
        else:
            while p.next!=None:
                p=p.next
            p.next=q
    def display(self):
        p=self.head
        l=1
        while p!=None:
            if p.coff>0:
                if l==1:
                  print(p.coff,"x^",p.exp,end="")
                else:
                  print("+",p.coff,"x^",p.exp,end="")
            else:
                print(p.coff,"x^",p.exp,end="")
            p=p.next
            l+=1
        print("\n")
def derivation(p1):
    p2=Polynomial()
    p=p1.head
    print("\nDerivation of polynimoal is:")
    while p!=None:
        p.coff=p.coff*p.exp
        p.exp-=1
        p2.insert(p.coff,p.exp)
        p=p.next
    p2.display()
    
p1=Polynomial()
while(1):
    print("1.For Insert")
    print("2.For Derivation")
    print("3.For Display")
    print("0.For Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        x=int(input("Enter coefficent value:"))
        y=int(input("Enter exponent value:"))
        p1.insert(x,y)
    elif ch==2:
        derivation(p1)
    elif ch==3:
        p1.display()
    else:
        break
