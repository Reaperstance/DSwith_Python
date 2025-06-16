class Counting:
    def count(self):
        l = list(map(int, input("Enter your chosen elements and please provide spaces for each entered elements! \n").split()))
        n = int(input("Enter the element that you wish to count the repeatation on the given list. \n"))
        c = 0  
        
        for i in l:
            if i == n:
                c += 1
        
        print("The element", n, "appears", c, "times.")

ob1 = Counting()
ob1.count()
