class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty!")
            return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty!")
            return None
    def size(self):
        return len(self.items)

class QueueUsingStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()
    def is_full(self):
        return self.enqueue_stack.size() + self.dequeue_stack.size() == self.max_size
    def is_empty(self):
        return self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty()
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
            return
        self.enqueue_stack.push(item)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        if self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                self.dequeue_stack.push(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Queue elements:")
        for item in reversed(self.enqueue_stack.items):
            print(item, end=" ")
        for item in self.dequeue_stack.items:
            print(item, end=" ")
        print()

max_size = int(input("Enter the maximum size of the queue: "))
queue = QueueUsingStack(max_size)
while True:
    print("\nQUEUE OPERATIONS")
    print("1. Enqueue element into queue")
    print("2. Dequeue element from queue")
    print("3. Display queue elements")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = input("Enter element to enqueue: ")
        queue.enqueue(element)
    elif choice == 2:
        dequeued = queue.dequeue()
        if dequeued is not None:
            print("Dequeued element:", dequeued)
    elif choice == 3:
        queue.display()
    elif choice == 4:
            print("Exiting program...")
            break
    else:
         print("Invalid choice! Please enter a valid option.")

