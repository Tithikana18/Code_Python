class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Linkedlist:
      def __init__(self):
          self.head=None
      def create(self,data):
          p=self.head
          q=Node(data)
          if p==None:
              self.head=q
          else:
              while p.next!=None:
                  p=p.next
              p.next=q
              q.prev=p
      def insert_beg(self,data):
          p=self.head
          q=Node(data)
          q.next=p
          p.prev=q
          self.head=q
      def insert_mid(self,data,sk):
          p=self.head
          q=Node(data)
          while p.next!=None:
              if p.data==sk:
                  q.next=p.next
                  q.next.prev=q
                  q.prev=p
                  p.next=q
              p=p.next
      def insert_end(self,data):
          p=self.head
          q=Node(data)
          while p.next!=None:
              p=p.next
          p.next=q
          q.prev=p
      def del_beg(self):
          p=self.head
          q=p.next
          self.head=q
          q.prev=None
          p.next=None
          del(p)
      def del_mid(self,sk):
          p=self.head
          while p.next!=None:
              if p.data==sk:
                  q=p.next
                  p.next=q.next
                  q.next.prev=p
                  q.next=None
                  q.prev=None
                  del(q)
              p=p.next
      def del_end(self):
          p=self.head
          while p.next.next!=None:
              p=p.next
          q=p.next
          q.prev=None
          p.next=None
          del(q)
      def display(self):
          p=self.head
          print("1.For Display The Node As The Order Of User Input")
          print("2.For Display The Node In Reverse Order")
          print("3.For Display The Node As The User Input And Reverse Order") 
          op=int(input("Enter an option:"))
          if op==1:
             while p!=None:
                 if p.next==None:
                     print(p.data)
                 else:
                     print(p.data,end="-->")
                 q=p
                 p=p.next
          elif op==2:
             while q!=None:
                  if q.prev==None:
                      print(q.data)
                  else:
                      print(q.data,end="<--")
                  q=q.prev
          elif op==3:
             while p!=None:
                  if p.next==None:
                       print(p.data)
                  else:
                       print(p.data,end="-->")
                  q=p
                  p=p.next
             while q!=None:
                  if q.prev==None:
                       print(q.data)
                  else:
                       print(q.data,end="<--")
                  q=q.prev
            
l1=Linkedlist()
while(1):
    print("1:For Create Node")
    print("2:For Insert Node At First")
    print("3:For Insert Node Between Any Node")
    print("4:For Insert Node At End")
    print("5:For Delete First Node")
    print("6.For Delete Any Node Between Two Node")
    print("7.For Delete Last Node")
    print("8.For Display")
    print("0.For exit")
    print("---------------------------------")
    choice=int(input("Enter your choice:"))
    if choice==1:
        n=int(input("Enter an element:"))
        l1.create(n)
    elif choice==2:
        x=int(input("Enter an element:"))
        l1.insert_beg(x)
    elif choice==3:
        y=int(input("Enter an element:"))
        pos=int(input("Enter an existing element after where you want to add an new element:"))
        l1.insert_mid(y,pos)
    elif choice==4:
        z=int(input("Enter an element:"))
        l1.insert_end(z)
    elif choice==5:
        l1.del_beg()
    elif choice==6:
        pos=int(input("Enter an existing element after where you delete a node:"))
        l1.del_mid(pos)
    elif choice==7:
        l1.del_end()
    elif choice==8:
        l1.display()
    else:
        break
    
                 
           
    
