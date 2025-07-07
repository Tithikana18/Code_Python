class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(Self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    def eva_postfix(self,expr):
        for char in expr:
            if char.isdigit():
                self.push(int(char))
            else:
                operand2=self.pop()
                operand1=self.pop()
                if operand1 is None or operand2 is None:
                    print("Invalid postfix expression.")
                    return None
                if char=='+':
                    result=operand1+operand2
                elif char=='-':
                    result=operand1-operand2
                elif char=='*':
                    result=operand1*operand
                elif char=='/':
                    if operand==0:
                        print("Division by zero error.")
                        return None
                    result=operand1/operand2
                else:
                    print("Invalid operator.")
                    return None
                self.push(result)
            if len(self.items)==1:
                return self.pop()
            else:
                print("Invalid postfix expression.")
                return None
s=Stack()
postfix_expr=input("Enter postfix expression:")
result=s.eva_postfix(postfix_expr)
if result is not None:
    print("Value of the postfix expression:",result)
                
