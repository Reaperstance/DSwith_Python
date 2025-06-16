class Rep:  
    def __init__(self, s):  
        self.s = s  

    def rep(self):  
        r = ""  
        for i in range(len(self.s)):  
            if i > 0 and self.s[i] == self.s[i-1]:  
                r += "*"  
            else:  
                r += self.s[i]  
        return r  

n = input("Enter a string: ")  
ob = Rep(n)  
print(ob.rep())  
