class ins:

    l1=[]

    def __init__(self, l):
        l=input("Enter the list: ").split()
        self.l1=l

    def insertion_sort(self):
        le=len(self.l1)
        i=1
        print("Here is the sorting process:")
        print("The unsorted list is: ", self.l1)
        while (i <  le):
            item=self.l1[i]
            ind=i-1
            while (ind >=0 and item < self.l1[ind]):
                self.l1[ind+1]=self.l1[ind]
                ind=ind-1
                print(self.l1, end="█")
                print()
            print(self.l1, end="█")
            print()
            self.l1[ind+1] = item
            i=i+1
        print("The sorted list is: ", self.l1)

ob1=ins([])
ob1.insertion_sort()