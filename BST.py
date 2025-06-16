class Node:
    
    def __init__(self, data):

        self.info = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):

        self.root = None

    def insert(self, item):

        nd = Node(item)

        if self.root == None:

            self.root = nd

            return

        par = temp = self.root

        while temp != None:

            par = temp

            if item < temp.info:

                temp = temp.left

            elif item > temp.info:

                temp = temp.right

            else:

                print("Repeated Values Has Occured. Ommiting the repeated values...")
                print()
                return

        if item < par.info:

            par.left = nd

        else:

            par.right = nd
                

    def inorder(self, temp):

        if temp != None:

            self.inorder(temp.left)

            print(temp.info, end=' ')

            self.inorder(temp.right)

    def postorder(self, temp):

        if temp != None:

            self.postorder(temp.left)

            self.postorder(temp.right)

            print(temp.info, end=' ')

                

    def preorder(self, temp):

        if temp != None:

            print(temp.info, end=' ')

            self.preorder(temp.left)

            self.preorder(temp.right)


b1 = BST()

print("Choose your desired option from thee following for this Birary Search Tree...")
print()

print("1. For Item Insertion")
print("2. For Preorder Arrangement")
print("3. For Postorder Arrangement")
print("4. For Inorder Arrangement")
print("5. For Displaying all the forms of Arragement")
print("6. For exit the interface")

while True:

    print()

    n = int(input("Enter your choice: "))

    if n == 1:

        item = int(input("Enter your item: "))

        b1.insert(item)

        while n == 1:

            print()
                        
            print("Do you wish to continue inserting item? Y/N")

            ch = input("Your choice? ")
            
            if ch == "Y" or ch == "y":

                item = int(input("Enter your item: "))

                b1.insert(item)

            else:

                print("Exiting insertion...")
                print()
                break


    elif n == 2:

        print()
            
        print("The preorder Arrangement: ")
            
        b1.preorder(b1.root)
            
        print()
            
                            
    elif n == 3:

        print()
            
        print("The postorder Arrangement: ")
            
        b1.postorder(b1.root)
            
        print()


    elif n == 4:

        print()
            
        print("The inorder Arrangement: ")
            
        b1.inorder(b1.root)
            
        print()


    elif n == 5:

        print()
            
        print("The Pre Order Arrangement: ")
            
        b1.preorder(b1.root)
            
        print()

        print()

        print("The In Order Arrangement: ")
            
        b1.inorder(b1.root)
            
        print()

        print()

        print("The Post Order Arrangement: ")
            
        b1.postorder(b1.root)

        print()
            
        print()


    elif n == 6:

        print()

        print("Exiting the program...")

        break


    else:

        print("Wrong input try Again")
            
                                   
