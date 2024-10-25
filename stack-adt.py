class node:
    def __init__(self,data):
        self.data=data
        self.next = None

class Stack:

    def __init__(self):
        self.head=None
        self.s=0

    def push(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        else:
            self.head.next=newnode
            self.head=newnode

    def pop(self):
        data=self.head.data
        self.head=self.head.next
        print(data)

    def peek(self):
        print(self.head.data)

    def is_empty(self):
        return self.head is None

stack=Stack()
n=int(input())
for i in range(n):
    op=input().split()

    if op[0]=="push":
        stack.push(op[1])
    elif op[0]=="pop":
        stack.pop()
    elif op[0]=="peek":    
        stack.peek()
    elif op[0]=="isEmpty":
        print(stack.is_empty())                                                
