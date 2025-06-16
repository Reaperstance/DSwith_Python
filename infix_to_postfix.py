class infix_to_postfix:
    def __init__(self, list1):
        self.infix = list1
        self.postfix = []
        self.stack = [0] * 20
        self.top = -1

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
       for i in range(0,len(self.infix)-1):
            if self.infix[i].isalpha():
               self.postfix.append(self.infix[i])

            elif self.infix[i] == '(':
              self.top += 1
              self.stack[self.top] = self.infix[i]

            elif self.infix[i] in ['+', '-', '*', '/', '^']:
                self.top += 1
                self.stack[self.top] = self.infix[i]
                if self.list[i]=='(':
                    self.top += 1
                    self.stack[self.top] = self.infix[i]
                    



            

            

    def display(self):
        print(self.infix)
        print(self.postfix)

ob = infix_to_postfix(['A', '+', '(', 'B', '-', 'C', ')', '/', 'D'])
ob.pfixconv()
ob.display()
