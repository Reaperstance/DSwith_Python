class Queue:
    def __init__(self, size):
        self.size = size
        self.list1 = [0 for _ in range(size)]
        self.rear = -1
        self.front = -1

    def push(self, item):
        if self.rear == self.size - 1:
            print("Queue Overflow. Insertion not possible.")
            return
        self.rear += 1
        self.list1[self.rear] = item
        if self.front == -1:
            self.front = 0
        print(f"{item} inserted into queue.")

    def pop(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow. Deletion not possible.")
            return -1
        item = self.list1[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        print(f"{item} removed from queue.")
        return item

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
        else:
            print("Queue elements:", self.list1[self.front:self.rear + 1])

queue_size = int(input("Enter the size of the queue: "))
q = Queue(queue_size)

while True:
    print("\nMenu:")
    print("1. Enqueue an element")
    print("2. Dequeue an element")
    print("3. Display queue")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        item = int(input("Enter element to enqueue: "))
        q.push(item)
    elif choice == '2':
        q.pop()
    elif choice == '3':
        q.display()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
