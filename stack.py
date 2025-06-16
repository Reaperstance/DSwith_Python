class Stack:
    def __init__(self, size):
        self.size = size
        self.list1 = [0 for _ in range(size)]
        self.top = -1

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack Overflow. Insertion not possible.")
            return
        self.top += 1
        self.list1[self.top] = item
        print(item, " inserted into stack.")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow. Deletion not possible.")
            return -1
        item = self.list1[self.top]
        self.top -= 1
        print(item, " removed from stack.")
        return item

    def display(self):
        if self.top == -1:
            print("Stack is empty.")
        else:
            print("The elements present in stacks are:")
            for i in range(self.top, -1, -1):
                print(self.list1[i])

stack_size = int(input("Enter the size of the stack: "))
st = Stack(stack_size)

while True:
    print("\n" "Enter your choice.")

    print("1. Push an element")

    print("2. Pop an element")

    print("3. Display stack")
    
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        item = int(input("Enter element to push: "))
        st.push(item)

    elif choice == '2':
        st.pop()

    elif choice == '3':
        print("\n")
        st.display()

    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
