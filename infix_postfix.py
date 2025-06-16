class InfixToPostfix:
    def __init__(self, expr):
        self.infix = expr
        self.postfix = []
        self.stack = []
    
    def precedence(self, op):
        if op in ['+', '-']:
            return 1
        elif op in ['*', '/']:
            return 2
        elif op == '^':
            return 3
        else:
            return 0
    
    def pfixconv(self):
        for char in self.infix:
            if char.isalnum():
                self.postfix.append(char)
            elif char == '(':
                self.stack.append(char)
            elif char == ')':
                while self.stack and self.stack[-1] != '(':
                    self.postfix.append(self.stack.pop())
                self.stack.pop()
            else:
                while self.stack and self.precedence(self.stack[-1]) >= self.precedence(char):
                    self.postfix.append(self.stack.pop())
                self.stack.append(char)
        
        while self.stack:
            self.postfix.append(self.stack.pop())
    
    def display(self):
        print("Postfix Expression:", ''.join(self.postfix))

exp = input("Enter infix expression: ")
ob = InfixToPostfix(exp)
ob.pfixconv()
ob.display()
