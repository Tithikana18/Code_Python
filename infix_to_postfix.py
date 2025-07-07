class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    def precedence(self,op):
        if op=='+' or op=='-':
            return 1
        elif op=='*' or op=='/':
            return 2
        elif op=='^':
            return 3
        else:
            return 0
    def infix_to_postfix(self,expr):
        postfix=''
        for char in expr:
            if char.isalnum():
                postfix+=char
            elif char=='(':
                self.push(char)
            elif char==')':
                while not self.is_empty() and self.peek()!='(':
                    postfix+=self.pop()
                self.pop()
            else:
                while not self.is_empty() and self.precedence(char)<=self.precedence(self.peek()):
                    postfix+=self.pop()
                self.push(char)
        while not self.is_empty():
            postfix+=self.pop()
        return postfix
s=Stack()
infix_expr=input("Enter infix expression:")
postfix_expr=s.infix_to_postfix(infix_expr)
print("Postfix expression:",postfix_expr)
            
                
