class NP:
    def __init__(self, n):
        self.n = n

    def disp(self):
        for i in range(5):
            print(self.n[i],end=' ')

a = input("Enter your name: ")
obj = NP(a)
obj.disp()
