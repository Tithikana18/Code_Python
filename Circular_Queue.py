class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*self.size
        self.front=self.rear=-1
    def enqueue(self):
        if (self.rear+1)%self.size==self.front:
            print("Circular Queue Is Full")
        else:
            if self.front==-1:
                self.front=0
            self.rear=(self.rear+1)%self.size
            data=int(input("Enter an element:"))
            self.queue[self.rear]=data
            print("Inserted element is:",data)
                
    def dequeue(self):
         if self.front==self.size-1 and falg==0:
             print("Circular Queue Is Empty")
         else:
             Temp=self.queue[self.front]
             print("Deleted element is:",Temp)
             if self.front==self.rear:
                 self.front=self.rear=self.size-1
                 flag=0
             else:
                 self.front=(self.front+1)%self.size
    def display(self):
         if self.front==self.size-1:
             print("Circular Queue is Empty")
         else:
             print("Queue element is:")
             n=self.front
             while n!=self.rear:
                 print(self.queue[n],end="->")
                 n=(n+1)%self.size
             print(self.queue[n])
Max_Size=int(input("Enter the size of the queue:"))
queue=CircularQueue(Max_Size)
while(1):
    print("1.For Insert")
    print("2.For Delete")
    print("3.For Display")
    print("0.Exit")
    print("--------------")
    ch=int(input("Enter your choice:"))
    if ch==1:
           queue.enqueue()
    elif ch==2:
           queue.dequeue()
    elif ch==3:
           queue.display()
    elif ch==0:
           print("Exit From The Program")
           break
    else:
        print("Invalid choice.please enter valid choice")
        
